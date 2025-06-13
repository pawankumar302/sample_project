import pandas as pd
import matplotlib.pyplot as plt

# Sample lead data
data = {
    'LeadID': [1, 2, 3, 4, 5, 6],
    'Campaign': ['Email', 'Social Media', 'Email', 'Webinar', 'Social Media', 'Webinar'],
    'Industry': ['IT', 'Finance', 'IT', 'Healthcare', 'Finance', 'Healthcare'],
    'Country': ['India', 'USA', 'India', 'UK', 'USA', 'UK'],
    'LeadStatus': ['Connected', 'Outreach', 'Connected', 'Interested', 'Outreach', 'Connected'],
    'Potential': ['High', 'Medium', 'Low', 'High', 'Low', 'Medium']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# ----------- FILTER SECTION ------------
# Filter by Campaign and Country
filtered_df = df[(df['Campaign'] == 'Social Media') & (df['Country'] == 'USA')]

# ----------- GRID VIEW (Tabular) ------------
print("GRID VIEW:")
print(filtered_df)

# ----------- CHART VIEW (Pie Chart by Industry) ------------
industry_counts = filtered_df['Industry'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(industry_counts, labels=industry_counts.index, autopct='%1.1f%%')
plt.title('Lead Distribution by Industry (Filtered)')
plt.show()
