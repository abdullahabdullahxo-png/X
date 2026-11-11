def main():



    nums = []
    while True:

        x = input("")
        if x not in ("+","=","-","*"):
            x = int(x)
            nums.append(x)
        elif x == "=": 
            nums.append(x)
            break
        else:
            nums.append(x)
   
    if nums[1] == "+":
        addition(nums,0)
    elif nums[1] =="-":
        subtraction(nums,0)
    elif nums[1] == "*":
        multiplication(nums,0)





def addition(nums, rece):
    
    
    total = 0
    while rece == "0"or rece != 0:           
        
        total = rece
        if total == "0":
            total = int(total)  

        for i in range(len(nums)):
            if nums[i] == "+":
                for j in range( i + 1 ,len(nums),2):
                    total += nums[j]

                    if nums[j + 1] == "=":
                        print(total)
                        break
        break




   
    while rece == 0:
        total = 0
        
        for i in range(0,len(nums),2):

            if nums[i + 1] == "-":
                total += nums[i]

                if total == 0:
                    total = str(total)
                
                subtraction(nums,total)
                break
            if nums[i + 1] == '*':
                total += nums[i]

                if total == 0 :
                    total = str(total)

                multiplication(nums, total)
                break
            
            else:
                total += nums[i]
                if nums[i + 1] == '=':
                    print(total)
                    break
           
        break
    
        





def subtraction(nums,rece):
    #مشكله الطرح مش بيطرح صح 


    
   
      
    total = 0
    while rece == "0"or rece != 0 :
        total = rece 

        if total == "0":
            total = int(total)

        for i in range(len(nums)):

            if nums[i] == "-":
                for j in range( i + 1 ,len(nums),2):
                    total = total - nums[j]
                    
                    if nums[j + 1] == "=":
                        print(total)
                        break
               
        break
    
    
    

    while rece == 0:

    
        
        total = 0
        for i in range(2,len(nums),2):

            if i == 2:
                total  = nums[0]

            if nums[i + 1] == "+":
                total = total - nums[i]

                if total == 0 :
                    total = str(total)

                addition(nums,total)
                break

            if nums[i + 1] == '*':
                total = total - nums[i]
                
            
                if total == 0 :
                    total = str(total)
            
                    multiplication(nums, total)
                    break

            else:
                total = total - nums[i]

                if nums[i + 1] =="=":
                    print(total)
                    break
            
        
        break
                
                    
        



def multiplication(nums, rece):
    
    
    total = 0
    while rece == "0"or rece != 0:           
       
        total = rece
        if total == "0":
            total = int(total)  

        for i in range(len(nums)):
            if nums[i] == "*":
                for j in range( i + 1 ,len(nums),2):
                    total *= nums[j]

                    if nums[j + 1] == "=":
                        print(total)
                        break
        break




   
    while rece == 0:
        total = 1
        
        for i in range(0,len(nums),2):

            if nums[i + 1] == "-":
                total *= nums[i]

                if total == 0:
                    total = str(total)
                subtraction(nums,total)
                break
            if nums[i + 1] == '+':
                total *= nums[i]

                if total == 0:
                    total = str(total)
                addition(nums, total)
                break

            
            else:
                total *= nums[i]
                if nums[i + 1] == '=':
                    print(total)
                    break
           
        break







main()
