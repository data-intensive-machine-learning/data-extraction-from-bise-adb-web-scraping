import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://results.biserawalpindi.edu.pk/Result_Detail?p={}&q=10&r=2022"
start_value = 800001
end_value = 815975
data = []
for value in range(start_value, end_value + 1):
    url = base_url.format(value)
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        Rollno = soup.find(id="lblRollNumber")
        Name=soup.find(id="lblName")
        n="Name:"
        Studenttype=soup.find(id="lblNameStudentType")
        type="StudentType:"
        Total=soup.find(id="lblTotal")
        t="Total:"
        Status=soup.find(id="lblStatus")
        status="Status:"
        student_status="ABSENT"
        student_status1="IMPROVED"
        student_status2="FEES ISSUE 1050/- Rupees"
        student_status4="PASS"
        Form=soup.find(id="lblFormID")
        id="FormId:"
        colon=":"
        
        subj1=soup.find(id="Repeater_result4_Label1_0")
        theory1=soup.find(id="Repeater_result4_Label2_0")
        theory2=soup.find(id="Repeater_result4_Label3_0")
        practical1=soup.find(id="Repeater_result4_Label5_0")
        marks1=soup.find(id="Repeater_result4_Label6_0")
            
                
        subj2=soup.find(id="Repeater_result4_Label1_1")
        theory3=soup.find(id="Repeater_result4_Label2_1")
        theory4=soup.find(id="Repeater_result4_Label3_1")
        practical2=soup.find(id="Repeater_result4_Label5_1")
        marks2=soup.find(id="Repeater_result4_Label6_1")
            
        subj3=soup.find(id="Repeater_result4_Label1_2")
        theory5=soup.find(id="Repeater_result4_Label2_2")
        theory6=soup.find(id="Repeater_result4_Label3_2")
        practical3=soup.find(id="Repeater_result4_Label5_2")
        marks3=soup.find(id="Repeater_result4_Label6_2")
            
        subj4=soup.find(id="Repeater_result4_Label1_3")
        theory7=soup.find(id="Repeater_result4_Label2_3")
        theory8=soup.find(id="Repeater_result4_Label3_3")
        practical4=soup.find(id="Repeater_result4_Label5_3")
        marks4=soup.find(id="Repeater_result4_Label6_3")
                
        subj5=soup.find(id="Repeater_result4_Label1_4")
        theory9=soup.find(id="Repeater_result4_Label2_4")
        theory10=soup.find(id="Repeater_result4_Label3_4")
        practical5=soup.find(id="Repeater_result4_Label5_4")
        marks5=soup.find(id="Repeater_result4_Label6_4")
            
        subj6=soup.find(id="Repeater_result4_Label1_5")
        theory11=soup.find(id="Repeater_result4_Label2_5")
        theory12=soup.find(id="Repeater_result4_Label3_5")
        practical6=soup.find(id="Repeater_result4_Label5_5")
        marks6=soup.find(id="Repeater_result4_Label6_5")

        subj7=soup.find(id="Repeater_result4_Label1_6")
        theory13=soup.find(id="Repeater_result4_Label2_6")
        theory14=soup.find(id="Repeater_result4_Label3_6")
        practical7=soup.find(id="Repeater_result4_Label5_6")
        marks7=soup.find(id="Repeater_result_Label3_6")
    
        if(Status.text == student_status1 or Status.text==student_status4 ):
            data.append({
                "Roll No": Rollno.text,
                "Name": Name.text,
                "Student Type": Studenttype.text,
                "Total": Total.text,
                "Status": Status.text,
                "Form Id": Form.text,
                "Subject1":subj1.text,
                "Theory1":theory1.text,
                "Theory2":theory2.text,
                "Practical1":practical1.text,
                "Marks1":marks1.text,
                "Subject2":subj2.text,
                "Theory3":theory3.text,
                "Theory4":theory4.text,
                "Practical2":practical2.text,
                "Marks2":marks2.text,
                "Subject3":subj3.text,
                "Theory5":theory5.text,
                "Theory6":theory6.text,
                "Practical3":practical3.text,
                "Marks3":marks3.text,
                "Subject4":subj4.text,
                "Theory7":theory7.text,
                "Theory8":theory8.text,
                "Practical4":practical4.text,
                "Marks4":marks4.text,
                "Subject5":subj5.text,
                "Theory9":theory9.text,
                "Theory10":theory10.text,
                "Practical5":practical5.text,
                "Marks5":marks5.text,
                "Subject6":subj6.text,
                "Theory11":theory11.text,
                "Theory12":theory12.text,
                "Practical6":practical6.text,
                "Marks6":marks1.text
            })
        else:
                 data.append({
                "Roll No": Rollno.text,
                "Name": Name.text,
                "Student Type": Studenttype.text,
                "Total": Total.text,
                "Status": Status.text,
                "Form Id": Form.text
                 })
        print( Rollno.text)
      
    else:
        print(f"Failed to retrieve data for value {value}.")
df = pd.DataFrame(data)
file_path = r"E:\BISE_Rawalpindi\student_data_supply.xlsx"  

df.to_excel(file_path, index=False)
