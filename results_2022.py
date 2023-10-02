import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL
base_url = "https://results.biserawalpindi.edu.pk/Result_Detail?p={}&q=3&r=2022"

# Define the range of values to increment
start_value = 330001
end_value = 333268
# end_value = 372269  # Adjust as needed

async def fetch_data(session, value):
    url = base_url.format(value)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.text()
            soup = BeautifulSoup(data, "lxml")
            
            Rollno = soup.find(id="lblRollNumber")
            Name = soup.find(id="lblName")
            Studenttype = soup.find(id="lblNameStudentType")
            Total = soup.find(id="lblTotal")
            Status = soup.find(id="lblStatus")
            Form = soup.find(id="lblFormID")
            
            result = {
                "Roll No": Rollno.text,
                "Name": Name.text,
                "Student Type": Studenttype.text,
                "Total": Total.text,
                "Status": Status.text,
                "Form Id": Form.text,
            }
            
            for i in range(6):
                subj = soup.find(id=f"Repeater_result_Label1_{i}")
                marks = soup.find(id=f"Repeater_result_Label3_{i}")
                if subj and marks:
                    result[subj.text] = marks.text

            print("Fetched Roll No:", Rollno.text)  # Print Roll No here
            return result
        else:
            print(f"Failed to retrieve data for value {value}.")
            return None

async def main():
    data = []
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, value) for value in range(start_value, end_value + 1)]
        results = await asyncio.gather(*tasks)
        
    
    results = [result for result in results if result is not None]
    
    df = pd.DataFrame(results)
    file_path = r"E:\BISE_Rawalpindi\student_data_2022.xlsx"
    df.to_excel(file_path, index=False)

if __name__ == "__main__":
    asyncio.run(main())
