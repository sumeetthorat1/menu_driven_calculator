while True:
    ch = int(input('\nEnter Choice\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\n'))

    match ch:
        case 1:
            print('+++Addition+++')
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            ans = a + b
            print('Addition is : ',ans)
        case 2:
            print('---Subtraction---')
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            ans = a - b
            print('Subtraction is :',ans)
        case 3:
            print('***Multiplication***')
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            ans = a * b
            print('Multiplication is : ',ans)
        case 4:
            print('///Division///')
            a = int(input('Enter First Number : '))
            b = int(input('Enter Second Number : '))
            ans = a / b
            print('Division is : ',ans)
        case 5:
            print('Exiting')
            break
        case _:
            print('Please enter valid choice')


            
            
            
            
