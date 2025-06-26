import os

def walk(path):
    
    for f in os.listdir(path):
        file=os.path.join(path,f)
        if os.path.isdir(file):
            walk(file)
        
        if os.path.isfile(file):
            if file.lower().endswith("config.py"):
                print(file)
            
def main():
    
    path=input("inserire path:")
    walk(path)
    
    
if __name__=="__main__":
    main()