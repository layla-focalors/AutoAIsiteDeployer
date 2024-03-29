import argparse

def main():
    parser = argparse.ArgumentParser(description='AI Learning Auto Deployer', prog='ai-learn')
    parser.add_argument('-t', '--type', type=str, help='Type of Using Deplyer Modeset(Netlify, FastAPI only)')
    parser.add_argument('-l', '--location', type=str, help='Location of the Html FileSet(Manual)')
    
    args = parser.parse_args()
    
    if(args.type == 'Netlify' or args.type == 'netlify' or args.type == 'NETLIFY'):
        print('Deploying to Netlify')
    elif(args.type == 'FastAPI' or args.type == 'fastapi' or args.type == 'FASTAPI'):
        print('Deploying to FastAPI')
    else:
        print('Invalid Type of Deployer ModeSet')
        
    if(args.location == None):
        print('No Location Specified')
        
if __name__ == '__main__':
    main()