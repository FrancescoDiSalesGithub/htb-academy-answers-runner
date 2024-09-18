import yaml
import base64
import requests


print("htb-answer-runner")
print("checking properties of yaml file")

try:
    
    with open("htb.yml","r") as htb_yaml_file:
        
        htb_yaml = yaml.safe_load(htb_yaml_file)
        
        for modules_item in htb_yaml["modules"]:
            if modules_item["owned"] == True:
                print("giving answers to module {}".format(modules_item["name"]))
                for questions in modules_item["questions"]:

                    answer_encoded = base64.b64encode(str(questions["answer"]).encode())

                    body = {"question_id":questions["question_id"],"answer":answer_encoded.decode().replace("Cg==","")}
                    request_htb = requests.post("https://academy.hackthebox.com/api/check/answer",json = body,headers={"Authorization":htb_yaml["bearer"],"Content-Type":"application/json"})
   
                    print(request_htb.text)
                    print("answer sent")
                    
except Exception as yaml_exception:
    print(yaml_exception)


