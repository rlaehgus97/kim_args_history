import argparse
from kim_args_history.db.utils import count, top

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    #print(msg)
    
    #argparse core functionality
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount')           
    parser.add_argument('-t', '--top')      
    parser.add_argument('-d', '--dt')  

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:   #args.scount == True
        print(f"-s => {args.scount}")
        # print command count
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
            # print command of specific date
        else:
            parser.error("error: you must use top arg with  date argument")
            #parser.print_help()

    else:
        # print instruction
        parser.print_help()
