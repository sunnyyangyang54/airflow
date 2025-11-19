def get_sftp():
    print("get_sftp test")

def regist(name,sex,*args):
    print(f"이름은 {name}이고 성별은 {sex}입니다.")
    print(name)
    print(sex)
    print(f"기타옵션들: {args}")

def regist3(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(email)
    if phone:
        print(phone)

def regist2(name,sex,**kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션: {kwargs} 입니다.')        
    email = kwargs['email'] or ''
    phone = kwargs['phone'] or ''
    if email:
        print(email)
    if phone:
        print(phone)    