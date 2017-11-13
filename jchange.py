# -*- coding: utf-8 -*-
#This probram changes given date to hiragana_date and return.
import re
import codecs
import json
import base64
import requests

def get_japanese_date(given_date):
    """与えられたファイルの中からひらがなとカタカナ、漢字の文字を抽出し、"japanese.json"に保存する。"""
    print("Now working...")
    dict_date = []
    date = codecs.open(given_date,"rt",encoding="utf-8")
    date = date.read().split("\n")
    japanese = u"[ぁ-ん一-龥ァ-ン一-龥]"
    japanese = re.compile(japanese)

    for line in date:
        m = re.match(japanese,line)
        if m:
            dict_date.append(line)
            print(line)

    first_file = codecs.open("japanese.json","w","utf-8")
    json.dump(dict_date,first_file,indent=2,sort_keys=True,ensure_ascii=False)
    first_file.close()
    for line in dict_date:
        print(line)
    print("Your date was changed into 'Japanese only'! Successflly saved as 'japanese.json'!")


def change_hiragana(given_date,x,goo_api_id):
    """given_dateの1つ目からxつ目までをひらがなに変換し、リスト化、"hiragana.json"に保存する。"""
    print("Now working...")
    japanese_json = open(given_date,"r")
    jsondate = json.load(japanese_json)
    jsondate = [x for x in jsondate[1:x+1]]
    sending_date = ",".join(jsondate)
    params = {"app_id":goo_api_id,"sentence":sending_date, "output_type":"hiragana"}
    responses = requests.post(
    "https://labs.goo.ne.jp/api/hiragana",
    params)
    print(responses.content)
    save_file = open("hiragana.json","wt")
    json.dump(responses.content,save_file)
    save_file.close()
    print("Your date was changed into 'hiragana only'.Successflly saved as 'hiragana.json'")

get_japanese_date("jawiki-latest-all-titles-in-ns0")
change_hiragana("japanese.json",3000,"212ddcfeb4b83a547a2fff60b117d2735babf01080854f1197bd7bfea6fb5a2d")
