import json

f = open("c:/temp/py/config.json")
try:                                        #попробовать выполнить этот блок кода
    res = json.load(f)
except json.decoder.JSONDecodeError as ex:        #описывает какие действия д.б. выполнены, в случае если возникла какая-то
    # проблема. Здесь можно явно указать какие именно ошибки могут возникнуть (json.decoder.JSONDecodeError).
    # Или можно не указывать вообще ошибку, тогда питон вопримет всевозможные ошибки
    #pass                                    #pass означает проигноировать возникабщие исключения
    print("Raised error is: ", ex)
    res = {}
finally: #блок который будет выполнен при любых обстоятельствах
    f.close()

print("res: ", res)