while True:
      password=input("Enter a password :")
      has_upper=False
      has_num=False
      has_special=False
      for char in password:
           if char.isupper():
                has_upper=True
           if char.isdigit():
                has_num=True
           if not char.isalnum():
                has_special=True
      if len(password)<=8:
            print("Password is too short")
      elif not has_upper:
            print("password must contain a uppercase")
      elif not has_num:
            print("password must contain a number")
      elif not has_special:
            print("password must contain a special character")
      else:
            print("strong password")
            break
