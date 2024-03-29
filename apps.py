import argparse
import modules.deploy as deploy
import modules.handler as handler

def main():
    parser = argparse.ArgumentParser(description='AI Learning Auto Deployer', prog='ai-learn')
    parser.add_argument('-t', '--type', type=str, help='Type of Using Deplyer Modeset(Netlify, FastAPI only)')
    parser.add_argument('-l', '--location', type=str, help='Location of the Html FileSet(Manual)')
    parser.add_argument('-u', '--git_url', type=str, help='Git URL of the Repository(Manual)')
    
    args = parser.parse_args()
    
    DEPLOY_SITE = None
    
    if(args.type == 'Netlify' or args.type == 'netlify' or args.type == 'NETLIFY'):
        print('Deploying to Netlify')
        DEPLOY_SITE = 'Netlify'
    elif(args.type == 'FastAPI' or args.type == 'fastapi' or args.type == 'FASTAPI'):
        print('Deploying to FastAPI')
        DEPLOY_SITE = 'FastAPI'
    else:
        print('Invalid Type of Deployer ModeSet')
        
    if(args.location == None):
        print('No Location Specified\nUsing Default Location: ./deploy')
        
    ORIGIN_HASH = handler.sha1_for_largefile(args.location)
    # deploy.makegit(args.location, args.git_url)
    
    # 1회는 무조건 실행 / first Deploy
    
    if(DEPLOY_SITE == 'Netlify'):
        print('Netlify Deployer is not Supported Yet')
        return None
        # while True:
        #     if(ORIGIN_HASH != handler.sha1_for_largefile(args.location)):
        #         print(f'[{deploy.gettime()}] Web File Changed\norigin {ORIGIN_HASH["Hash"]} : now {handler.sha1_for_largefile(args.location)["Hash"]}')
        #         ORIGIN_HASH = handler.sha1_for_largefile(args.location)
                
        #         if(DEPLOY_SITE == 'Netlify'):
        #             pass
    elif(DEPLOY_SITE == 'FastAPI'):
        log = deploy.deploy_to_fastapi(args.location, args.git_url)
        print(log)
    else:
        print('Invalid Deployer ModeSet')
        
            # deploy.makegit(args.location, args.git_url)
    
    # print(handler.sha1_for_largefile(args.location))
if __name__ == '__main__':
    main()