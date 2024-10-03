# File Statistika_Colab.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from typing import Union, List



class Statistika:
    def __init__(self, Data: List[Union[int, float]]):
        if len(Data) == 0:
            raise ValueError("Data tidak boleh kosong.")
        self.Data = pd.Series(Data)

#A. Statistika Deskriptif
class StatistikDeskriptif(Statistika):
    # Menampilkan data awal    
    def info_data(self) -> pd.Series:
        return self.Data
    
    # Mengurutkan Data secara ascending  
    def sort(self) -> pd.Series:
        return self.Data.sort_values().reset_index(drop=True)

#1. Uuran Pemusatan Data    
    # Mean
    def mean(self) -> float:
        return self.Data.mean()
    # Median
    def median(self) -> float:
        return self.Data.median()
    # Mode 
    def mode(self) -> List[Union[int, float]]:
        mode_values = self.Data.mode().tolist()
        if len(mode_values) == len(self.Data.unique()):
            return ["tidak ada mode, semua nilai unik."]
        return mode_values

#2. Ukuran Penyebaran Data   
    # Range Data
    def data_range(self) -> float:
       return self.Data.max() - self.Data.min()
    # Kuartil
    def quartile(self) -> dict:
       Q1 = self.Data.quantile(0.25)
       Q2 = self.Data.median()
       Q3 = self.Data.quantile(0.75)
       return {"Q1" : Q1, "Q2" : Q2, "Q3" : Q3}
    # Interkuartil
    def interquartile(self) -> float:
        Q1 = self.Data.quantile(0.25)
        Q3 = self.Data.quantile(0.75)
        return Q3 - Q1
    # Outlier
    def outlier(self) -> List[Union[int, float]]:
        Q1 = self.Data.quantile(0.25)
        Q3 = self.Data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outlier = self.Data[(self.Data < lower_bound) | (self.Data > upper_bound)]
        return outlier.tolist()
    # Variance
    def variance(self) -> float:
     	return self.Data.var()     	
    # Standard Deviation
    def std_dev(self) -> float:
    	return self.Data.std()

#3.Data Distribusi     
    # Skewness
    def skewness(self) -> float:
    	return stats.skew(self.Data)
    # Kurtosis
    def kurtosis(self) -> float:
    	return stats.kurtosis(self.Data)
    # Frequency table
    def frequency_table(self) -> pd.DataFrame:
        frequency = pd.Series(self.Data).value_counts().sort_index()
        frequency_table = pd.DataFrame({
            'Value': frequency.index,
            'Frequency': frequency.values
        })
        print(frequency_table)
        return frequency_table
    
#4. Visualisasi Data
    # Histogram
    def histogram(self):
    	plt.hist(self.Data,bins='auto',alpha=0.7, rwidth=0.85)
    	plt.title('Histogram')
    	plt.show()
    # Box Plot
    def box_plot(self):
    	plt.boxplot(self.Data)
    	plt.title('Box Plot')
    	plt.show()
    # Pie Chart
    def pie_chart(self) -> None:
        labels = self.Data.value_counts().index
        sizes = self.Data.value_counts().values
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal') 
        plt.title('Pie Chart')
        plt.show()
    # Bar Chart
    def bar_chart(self) ->None:
    	counts = self.Data.value_counts()
    	counts.plot(kind='bar')
    	plt.title('Bar Chart')
    	plt.xlabel('Data')
    	plt.ylabel('Frequency')
    	plt.show()
    # Scatter Plot
    def scatter_plot(self,other_data: list[Union[int,float]]) -> None:
    	if(len(other_data) != len(self.Data)):
    		raise ValueError("Panjang data harus sama untuk scatter plot.")
    	plt.scatter(self.Data,other_data)
    	plt.title('Scatter Plot')
    	plt.xlabel('Data 1')
    	plt.ylabel('Data 2')
    	plt.show()
    # Dot Plot
    def dot_plot(self) -> None:
       counts = self.Data.value_counts().sort_index() 
       unique_values = counts.index  
       frequencies = counts.values
       plt.figure(figsize=(10, 6))
       for i, value in enumerate(unique_values):
          plt.plot([value] * frequencies[i], range(1, frequencies[i] + 1), 'ro', markersize=10)

       plt.title('Dot Plot')
       plt.xlabel('Data Values')
       plt.ylabel('Frequency')
       plt.show()
    



 
#B. Statistika Inferensial
    # fungsi class
#1. Pengujian Hipotesis
    # Hipotesis Nol(H0)
	# Hipotesis Alternatif(H1)
	# Uji-T (T-test)
	# Uji-Z
	
#2. Confidence Interval
	# Estimasi interval untuk parameter populasi
	
#3. Uji Signifikasi
	# p-value
	# Alpha level(a)
	
#4. Regresi dan Korelasi
	# Regresi Linier
	# Korelasi
	# ANOVA(Analysis of Variance)
	
#5. Distribusi Sampling
	# Distribusi Normal
	# Distribusi Binomial
	# Distribusi t-Student
	
#6. Analisis Chi-Square(X^2)
	# Uji hubungan antar variable kategorikal



# Pengolahan Input dengan Error Handling lebih baik
def input_data() -> List[Union[int, float]]:
    while True:
        try:
            input_data = input("Masukan angka integer atau float (pisahkan dengan koma): \n")
            # Memisahkan input, dan memastikan input dipecah dengan baik
            data = [float(num.strip()) for num in input_data.split(',')]
            if len(data) == 0:
                raise ValueError("Data tidak boleh kosong.")
            return data
        except ValueError as ve:
            print("Input tidak valid, pastikan memisahkan angka dengan koma:", ve)

# Penggunaan fungsi
data = input_data()
data_analisis = StatistikDeskriptif(data)

print("Data awal:\n", data_analisis.info_data())
print("Data sorting:\n", data_analisis.sort())
print("Data mean:", data_analisis.mean())
print("Data median:", data_analisis.median())
print("Data mode:", data_analisis.mode())
print("Data range:", data_analisis.data_range())
print("Data quartile:", data_analisis.quartile())
print("Data interquartile:", data_analisis.interquartile())
print("Data outlier:", data_analisis.outlier())
print("Skewness:",data_analisis.skewness())
print("Variance: ", data_analisis.variance())
print("Standar Devisiasi: ", data_analisis.std_dev())