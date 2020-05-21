"""
Copyright 2019, All rights reserved.
Author : SangJae Kang
Mail : rocketgrowthsj@gmail.com
"""
import json
import numpy as np
import pandas as pd
import tensorflow as tf
from .utils import print_with_tag
import os
import re
from .config import EVALUATION_URL, SAVE_DIR, DOWNLOAD_URL
from requests.auth import HTTPBasicAuth
from requests import Session
from getpass import getpass


class Tutor:
    def __init__(self, global_var, content="", section="", title=""):
        self.globals = global_var
        self.content = content
        self.section = section
        self.title = title
        self._sess = Session()

        if int(tf.__version__[0]) < 2:
            print_with_tag("텐서플로우는 2.x 이상으로 설치되어 있어야 합니다.", "WARNING")

        self.login()

    def login(self):
        while True:
            user_id = input("User ID : ")
            password = getpass('password : ')

            response = self._sess.get(EVALUATION_URL+"/login",
                                      params={"content": self.content},
                                      auth=HTTPBasicAuth(user_id, password))
            if response.status_code == 200:
                print_with_tag("{}으로 접속되었습니다.".format(user_id), "okgreen")
                break
            elif response.status_code == 401:
                print_with_tag("ID와 PW가 올바르지 않습니다. 다시 시도해주세요".format(user_id), "fail")
            elif response.status_code == 403:
                print_with_tag("해당 ID는 강좌 수강신청이 되어 있지 않습니다.", "fail")
                break
            else:
                print(response)
                break

    def evaluate(self, answer, title=None, content=None, section=None):
        title = self.title if title is None else title
        content = self.content if content is None else content
        section = self.section if section is None else section

        params = {"content": content,
                  "section": section,
                  "title": title}

        answer = encode_answer(answer)
        answer['source'] = get_source_code(self.globals.get('In'))

        response = self._sess.post(EVALUATION_URL+"/evaluation", params=params, data=answer)

        if response.status_code // 100 == 2:
            result = json.loads(response.content)
            message = result.get('message', '')

            if result.get('result', False):
                print_with_tag("축하합니다! 정답입니다!")
                print_with_tag(message, 'okblue')
                return True
            else:
                print_with_tag("아쉽게도 틀렸습니다.", "fail")
                print_with_tag(message, 'fail')
                return False

        elif response.status_code == 401 or response.status_code == 403:
            print_with_tag("우선 로그인부터 해주세요", "fail")
            self.login()

        elif response.status_code == 500:
            print_with_tag("서버에서 올바르게 동작하지 않습니다.", "fail")
            return False

        else:
            print_with_tag("서버에서 올바르게 응답하지 않습니다", "fail")

            try:
                print(str(response.content))
            except:
                print(response.content)

            return response

    def load_data(self, data_type, title=None, content=None, section=None, refresh=False):
        title = self.title if title is None else title
        content = self.content if content is None else content
        section = self.section if section is None else section

        fname = "{}-{}-{}-{}.npz".format(content, section, title, data_type)
        save_path = os.path.join(SAVE_DIR, fname)

        if refresh or not os.path.exists(save_path):
            with open(save_path, 'wb') as f:
                req = self._sess.get(DOWNLOAD_URL+'/'+fname)
                f.write(req.content)

        return dict(np.load(save_path, allow_pickle=True))


def encode_answer(answer):
    if isinstance(answer, str):
        data_type = 'str'
        answer = str(answer)
    elif isinstance(answer, bool):
        data_type = 'bool'
        answer = json.dumps(answer)
    elif isinstance(answer, int):
        data_type = 'int'
        answer = str(answer)
    elif isinstance(answer, float):
        data_type = 'float'
        answer = str(answer)
    elif isinstance(answer, complex):
        data_type = 'complex'
        answer = str(answer)
    elif isinstance(answer, tuple):
        data_type = 'tuple'
        answer = json.dumps(answer)
    elif isinstance(answer, set):
        data_type = 'set'
        answer = json.dumps(list(answer))
    elif isinstance(answer, dict):
        data_type = 'dict'
        answer = json.dumps(answer)
    elif isinstance(answer, list):
        data_type = 'list'
        answer = json.dumps(answer)
    elif isinstance(answer, np.ndarray):
        data_type = 'np.ndarray'
        answer = json.dumps(answer.tolist())
    elif isinstance(answer, pd.Series):
        data_type = 'pd.Series'
        answer = answer.to_json()
    elif isinstance(answer, pd.DataFrame):
        data_type = 'pd.DataFrame'
        answer = answer.to_json()
    elif isinstance(answer, tf.Tensor):
        data_type = 'tf.Tensor'
        answer = json.dumps(answer.numpy().tolist())
    elif isinstance(answer, tf.keras.Model):
        data_type = 'tf.keras.Model'
        answer = answer.to_json()
    else:
        type_answer = type(answer)
        raise TypeError("{}은 지원하지 않는 데이터 형입니다.".format(type_answer))
    return {
        "data_type": data_type,
        "answer": answer
    }


def get_source_code(codes, count=10):
    evaluation_code = codes[-1]
    curr_eval_flag = True

    answer_codes = []
    for code in codes[::-1]:
        if count == 0:
            break

        if curr_eval_flag and code == evaluation_code:
            continue
        elif re.findall('\s*evaluate\(.+, .+\)\s*', code):
            break

        curr_eval_flag = False
        answer_codes.append(code)
        count -= 1

    return "\n".join(answer_codes[::-1])
