import streamlit as st 
# EDA Pkgs
import pandas as pd 
import numpy as np 
# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
# Components Pkgs
import streamlit.components.v1 as components
# Custome Component Fxn 




footer_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">About Automated EDA</h5>
	          <p class="grey-text text-lighten-4">Using Streamlit,Pandas,Numpy,Matplotlib,Seaborn.</p>
	        </div>
	      
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Me</h5>
	          <ul>
	         
	          <a href="https://www.linkedin.com/in/muskan-thakur-a81752181/" target="_blank" class="white-text">
	            <i class="fab fa-linkedin fa-4x"></i>
	          </a>
	       
	          </ul>
	        </div>
	      </div>
	    </div>
	    <div class="footer-copyright">
	      <div class="container">
	      Made by <a class="white-text text-lighten-3" >Muskan Thakur</a><br/>
	      </div>
	    </div>
	  </footer>
	"""
def main():
	"""Automated Exploratory Data Analysis"""

	menu = ["Home","EDA","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == 'EDA':
		st.subheader("Exploratory Data Analysis")

		data = st.file_uploader("Upload a File", type=["csv", "txt"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())
			

			if st.checkbox("Shape"):
				st.write(df.shape)

			if st.checkbox("Columns"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			if st.checkbox("Selected Columns"):
				selected_columns = st.multiselect("Select Columns",all_columns)
				new_df = df[selected_columns]
				st.dataframe(new_df)
                
			if st.checkbox("Value Counts"):
				st.write(df.iloc[:,-1].value_counts())
                
			if st.checkbox("Summary"):
				st.write(df.describe())                

			if st.checkbox("Correlation Plot(Matplotlib)"):
				plt.matshow(df.corr())
				st.pyplot()

			if st.checkbox("Correlation Plot(Seaborn)"):
				st.write(sns.heatmap(df.corr(),annot=True))
				st.pyplot()
                
			# Customizable Plot

			all_columns_names = df.columns.tolist()
			type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
			selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

                
			if st.checkbox("Generate plot"):
				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

				# Plot By Streamlit
				if type_of_plot == 'area':
					cust_data = df[selected_columns_names]
					st.area_chart(cust_data)

				elif type_of_plot == 'bar':
					cust_data = df[selected_columns_names]
					st.bar_chart(cust_data)

				elif type_of_plot == 'line':
					cust_data = df[selected_columns_names]
					st.line_chart(cust_data)

				# Custom Plot 
				elif type_of_plot:
					cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
					st.write(cust_plot)
					st.pyplot()                
                
                


	elif choice == "About":
		st.subheader("About App")
		components.html(footer_temp,height=500)
		

                    
	else:
		st.subheader("Home")
		html_temp = """
		<div style="background-color:royalblue;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Automated Exploratory Data Analysis</h1>
		</div>
		"""


		components.html(html_temp)

		components.html("""
			  <img src="https://favtutor.com/resources/images/uploads/Covid_19_data_analysis.jpg" style="width:40%">
			
			""")
		components.html("<p style='color:black;'> In statistics, exploratory data analysis is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task. Exploratory data analysis was promoted by John Tukey to encourage statisticians to explore the data, and possibly formulate hypotheses that could lead to new data collection and experiments. EDA is different from initial data analysis, which focuses more narrowly on checking assumptions required for model fitting and hypothesis testing, and handling missing values and making transformations of variables as needed.</p>")            
		components.html("<p style='color:black;'>In data mining, Exploratory Data Analysis (EDA) is an approach to analyzing datasets to summarize their main characteristics, often with visual methods. EDA is used for seeing what the data can tell us before the modeling task. It is not easy to look at a column of numbers or a whole spreadsheet and determine important characteristics of the data. It may be tedious, boring, or overwhelming to derive insights by looking at plain numbers. Exploratory data analysis techniques have been devised as an aid in this situation.</p>")           
		components.html("<p style='color:black;'>The EDA types of techniques are either graphical or quantitative (non-graphical). While the graphical methods involve summarising the data in a diagrammatic or visual way, the quantitative method, on the other hand, involves the calculation of summary statistics. These two types of methods are further divided into univariate and multivariate methods. The EDA approach is not just a set of techniques, but an attitude about how data analysis should be carried out. </p>")
                   
                
                
                

                


if __name__ == '__main__':
	main()