import os 
import argparse
import requests
import json
def  main():
    parser = argparse.ArgumentParser(
                    prog='TechAI Interview helper',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    
    parser.add_argument('-r', '--resume') 
    args = parser.parse_args()
    resume = args.resume
    print(f'Analyzing resume: {resume}')
    ### here would chat gpt using api create our question... 
    ### dummy parser 
    type_project = 'nextjs'
    code_from_gpt = ''
    appname = 'demoapp'
    #if type_project == 'nextjs':
    #    os.system(f'npx create-next-app {appaname} --ts --tailwind --eslint --app')
    body = {
        'resume' : 'resume.pdf',
        'prompt' : 'some prompt dsjahjdsajhdksajkdsa'
    }
    response  = requests.post('http://localhost:3000/createQuestion', data=body)
    data = response.json()
    print(data)

    os.system(f"echo '{data['code_']}'  > {appname}/app/page.tsx")

if __name__ == '__main__':
    main()