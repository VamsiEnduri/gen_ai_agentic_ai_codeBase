# # # # # # day 1 :-- gen ai / agentic ai 
# # # # # # python 
# # # # # # sql 
# # # # # # pandas
# # # # # # plotly

# # # # # # next 4 dys


# # # # # conditions 
# # # # # logical and membership ops 
# # # # # for loop list of dict,tuples 
# # # # # modules :-- third party , json 
# # # # # functions  :-- 
# # # # # scopes
# # # # # try except


# # # # # select 
# # # # # insert 
# # # # # update
# # # # # delete 
# # # # # create 
# # # # # dtypes
# # # # # constraints
# # # # # joins  :-- inner joins


# # # # # pandas ?
# # # # # features ?
# # # # # dtaFrame ?
# # # # # how to create dtaFrame ?
# # # # # accessing dtaFrame and dtaFramecolumns
# # # # # applying conditions 
# # # # # applying accessing methods 




# # # # # plotly
# # # # # importing plotly 
# # # # # 4 charts 
# # # # # bar 
# # # # # line
# # # # # area
# # # # # pie


# # # # # conditions  statements
# # # # # if 
# # # # if [] == []:
# # # #     print("vamsi")
# # # #     print(10000)
# # # #     print("10000coders")
# # # # # if-else
# # # # if [] == []:
# # # #     print("vamsi")
# # # #     print(10000)
# # # #     print("10000coders")
# # # # else :
# # # #     print("condition didnt satisfied")    
# # # # # elif ladder

# # # # if True :
# # # #     print("asdfgh")
# # # # elif True/False:
# # # #     print("asdfghjk")
# # # # elif True/False:
# # # #     print("ASDFGHJK")
# # # # else:
# # # #     print("asdfg")            

# # # # # nested if 
# # # # if True :
# # # #     if True:
# # # #         print("asdfgh")
# # # #     else:
# # # #         print("qwertyu")
# # # # else:
# # # #     if True:
# # # #         print("q3456789")
# # # #     else :
# # # #         print("zxcvbwert123456")               

# # # # #  logical and membership ops 
# # # # and  :-- lo and ro :-- True
# # # # print(10 ==10 and "vamsi" == "vamsi") # True
# # # # or  :-- lo or ro :-- True / True / False 
# # # # print(city == "hyd" or salary >25000) @null rows
# # # # not :-- vice versa opposite
# # # # is_loggedinStatus=True  #login
# # # # is_loggedinStatus = not is_loggedinStatus #logout False


# # # # in  :-- check availability  it is there r not
# # # # print("v" in "10000coders")  # False
# # # # print("abc" in "abdcabc") # True
# # # # not in  :-- check un-availability of item


# # # # print("v" not in "10000Coders") # True 
# # # # print("1000" not in [1,10,100,1000]) # True




# # # # # for loop list of dict,tuples 

# # # # # for i in/not in seq/range():
# # # # #     #code 

# # # # # for i in range(1,11):
# # # # #     print(i)
# # # # #     if i == 3:
# # # # #         continue

# # # # for i in range(1,11): # i=3
# # # #     if i ==2:
# # # #         continue
# # # #     if i == 3:
# # # #         break
# # # #     print(i) # 1




# # # # for i in "vamsi":
# # # #     print(i)

# # # # for i in [1,2,3,11,22,33,44,55]:
# # # #     print(i)    

# # # # for i in {"id":1,"name":"vamsi"}.items():
# # # #     print(i) # (id, 1) ("name","vamsi")

# # # # for i in (1,2,3,4):
# # # #     print(i)    




# # # #      #   modules

# # # # modules are nothing but py file which is contains var, class, functions
# # # # and we can import one module code to another module (another file)     

# # # # user-defined 
# # # # in-built :-- json, dattetime, re, random, math, etc..
# # # # third party :-- pandas, numpy, plotly, scikit learn etc..



# # # # # functions 
# # # # block of code that can be resuable whenever we call it 

# # # # def abc(): #define / creating
# # # #     print("1234567")
# # # #     a=100
# # # #     b=200
# # # #     print(a+b)
# # # # abc()   # calling / invocation


# # # # abcdef=1000 # global var
# # # # def abc():
# # # #     a=10 # abc scoped var
# # # #     def xyz():
# # # #         print(a)  # 
# # # #         x=1000 # xyz scoped varible
# # # #         y=20000
# # # #         z=x+y
# # # #         print(z)
# # # #     xyz()
# # # # abc()        



# # # # count = 5

# # # # def increase():
# # # #     count = count + 1
# # # #     print(count)

# # # # increase()


# # # # # try except
# # # try :
# # #     a=10
# # #     print(a+"10")
# # # except ZeroDivisionError:
# # #     print("something wrong")  
# # # except ValueError:
# # #     print("asdfghj")    
# # # except NameError:
# # #     print("asdfgh")
# # # else:
# # #     print("1234567")  


# # SQl :-- 

# # select :-- to select te columns from the existing table 
# # delete :-- to dletee the rows from table based on condition
# # update :-- to modify the data in the table r to add new data into specific columns 
# # insert :-- to insert the data into table as new rows 
# # create :-- to create table r db 
# # dTypes :-- char, varchar, date, decimal, boolean, int, text,enum() etc..
# # constraints :-- pk,fk,not null, default, unique, check ,auto_increment

# # pk vs fk 
# # unique values + not null  
# # fk is used to maintain realtionsgip with table to table 2 with ref col 
# # check() :-- to apply condition on specific col 
# # unique :-- maintain unique values in that column 


# # create table employees (
# # emp_id int primary key auto_increment,
# # emp_name varchar(50) not null,
# # emp_email varchar(50) unique not null, 
# # emp_dept enum("dev","sales","aws","devops","testing") default "sales",
# # emp_salary decimal(10,2) not null ,
# # emp_marriedStatus bool ,
# # emp_joining_date date ,
# # emp_age int check(emp_age > 21)
# # )



# # select *
# # from employees
# # where emp_age > 22 and emp_salary >25000 and emp_loc = "Hyd"


# # set sql_safe_updates = 0 :-- 
# # set autocommit = 0

# # delete from employees 
# # where emp_id >=5 and emp<=10

# # rollback;

# # delete from employees 
# # where emp_id >=6 and emp<=10

# # commit;

# # update employees 
# # set emp_salary = 34000,emp_loc="gacchibowli"
# # where emp_id = 10 and emp_name ="vamsi"



# # insert into employees ()
# # values (1,"vamsi","dev","123456","hyd","11-11-1111");



# # # joins :-- 
# # joins are used to combine multiple tables 

# # inner join is used to select matched rows 
# # synatx :-- 

# # select cls 
# # from table1 
# # inner join table 2 
# # on table1.ref_cl = table2.ref_cl 
# # # using ()


# # pandas :-- 
# # pandas is a python package which is used to perform opeartions on table kind of data which is nothing but dataFrame
# # and
# # the opeartions are 
#   # cleaning  # 
#   # analysis
#   # files read and create  #

# # pandas ?
# # dataFrame ? # table like data with rows and columns
# # dataFrame create ?
# # dataFrame look like what ?
# # dataFrame columns how to access ?
# # dataFrame data filter ? with one condition and multiple conditions ?
# # creating file with data ?


# # pip install pandas 
import pandas as pd 

# # creating dataFrame with dict 
# # emp1= {
# #     "id":1,
# #     "name":"vamsi",
# #     "company":"10000coders"
# # }

# # df=pd.DataFrame(emp1,index=[0]) # 
# # print(df,"302")

# emps = [ # data  list of lists
#     [1,"vamsi",30000],
#     [2,"ravi",45000],
#     [3,"ramesh",23000]
# ]


# df=pd.DataFrame(emps,columns=["Id","Name","Salary"]) # creating df
# # print(df)


# # print(df["Salary"]) # accessing single col
# # print(df[["Salary","Id"]]) # accesing mul col

# # rea pt 3 :-- how to access specifc columsn and specific rows 
# # filtering with singel condition :-- 

# # print(df[ df["Id"] >=2 ])
# # print(df[ df["Salary"] == 45000  ])


# print(df[ ( df["Id"] >=2 ) | ( df["Salary"] >= 40000) ])

# pandas :--
# creating dataFrame
# accessing columns
# applying filtering over the dataFrame using columns and logical oprs 


# list of dicts :--

data =[{"id":1,"name":"vamsi"},{"id":2,"name":"ravi"}]
df =pd.DataFrame(data)
print(df)
