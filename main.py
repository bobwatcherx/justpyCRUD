from justpy import *
import random


def Myapp():
	app = QuasarPage(data={
		# NOW I CREATE STATE LIKE VUE JS
		"todo":[],
		"nametxt":"",
		"agetxt":"",
		"idtxt":0
		})
	def getdatafromclick(self,msg):
		# THIS WILL GET TEXT FROM YOu SELECT LIST
		value = self.text
		getid = value.split("-")[0].strip()
		getname = value.split("-")[1].strip()
		getage = value.split("-")[2].strip()
		# AND NOW SET state TODO to you click list from list
		msg.page.data['nametxt'] = getname
		msg.page.data['agetxt'] = getage
		msg.page.data['idtxt'] = getid
		btnadd.show = False
		btnedit.show = True
		btndelete.show = True

	



	def addnewproses(self,msg):
		# GET ALL STATE TODO
		todo = app.data['todo']
		todo.append({
			# I CREATE RANDOM ID
			"id":random.randint(1,800),
			"name":name.value,
			"age":int(age.value),
			})
		print(todo)
		# THIS WILL REFRESH DATA AND LOAD NEW DATA TODO AGAIN
		mylist.delete_components()
		for x in app.data['todo']:
			myitem = QItem(clickable=True,
				v_ripple=True,
				a=mylist
				)
			byclick = QItemSection(text=f"{x['id']} - {x['name']} - {x['age']} ",a=myitem)
			byclick.on("click",getdatafromclick)
			reset_all_you(msg.page)


	def editproses(self,msg):
		youid = int(app.data['idtxt'])
		todo_list = app.data['todo']
		name = app.data['nametxt']
		age = app.data['agetxt']
		# NOW I WILL LOOP AND FIND ID IF FOUND THEN CHANGE NAME AGE
		for x in todo_list:
			if x['id'] == youid:
				x['name'] = name
				x['age'] = int(age)
				print(msg.page.data['todo'])
			else:
				print("kosong")
		print(app.data['todo'])
		# AND REFRESH DATA IN LIST
		mylist.delete_components()
		for x in app.data['todo']:
			myitem = QItem(clickable=True,
				v_ripple=True,
				a=mylist
				)
			byclick = QItemSection(text=f"{x['id']} - {x['name']} - {x['age']} ",a=myitem)
			byclick.on("click",getdatafromclick)
			reset_all_you(msg.page)


	def deleteproses(self,msg):
		# AND NOW DELETE PROSES 
		name = app.data['nametxt']
		age = app.data['agetxt']
		todo_list = app.data['todo']
		todo_copy = list(todo_list)
		# AND IF FOUND NAME AND AGE IS EQUAL THEN REMOVE 
		try:
			for x in todo_copy:
				if x['name'] == name and x['age'] == int(age):
					todo_list.remove(x)
		except Exception as e:
			print(e)
			print("errror")
		# AND REFRESH LIST
		mylist.delete_components()
		for x in app.data['todo']:
			myitem = QItem(clickable=True,
				v_ripple=True,
				a=mylist
				)
			byclick = QItemSection(text=f"{x['id']} - {x['name']} - {x['age']} ",a=myitem)
			byclick.on("click",getdatafromclick)
		reset_all_you(msg.page)



	# NOW I WILL CREATE FUNCTION FOR RESET 
	def reset_all_you(page):
		# CLEAR INPUT AND HIDE EDIT AND DELETE BUTTON
		# IF YOU FINISH CHANGEEDIT AND DELETe
		page.data['nametxt'] = ""
		page.data['agetxt'] = ""
		btnadd.show = True
		# HIDE EDIT DELETE BUTTON
		btnedit.show = False
		btndelete.show = False



	layout = Div(classes="q-pa-md column",a=app)
	# a is you parent compoennt
	name = QInput(
		placeholder="input name",
		# INSERT V-model here
		model=[app,"nametxt"],
		a=layout
		)
	age = QInput(
		placeholder="input age",
		# INSERT V-model here
		model=[app,"agetxt"],
		a=layout
		)
	btnadd = QBtn(classes="q-mt-md",
		label="Add new todo",
		color="green",a=layout
		)

	# NOW I CREATE LIST TILE
	mylist = QList(
		dense=True,
		bordered=True,
		padding=True,
		a=layout
		)

	# AND NOW I CREATE BUTTON EDIT AND DELETE BUTTON
	# THIS WILL SHOW IF YOU CLICK LIST TILE AND HIDE GREEN BUTTON
	myeditdeletebutton = Div(
		classes="q-pa-md row justify-around",
		a=layout
		)	
	btnedit = QBtn(
		label="edit",
		color="blue",
		show=False,
		a=myeditdeletebutton
		)
	btndelete = QBtn(
		label="delete",
		color="red",
		show=False,
		a=myeditdeletebutton
		)

	# AND NOW I WILL CREATE BUTTON LISTENER
	# IF YOU CLICK BUTTON THEN RUN FUNCTION
	btnadd.on("click",addnewproses)
	btnedit.on("click",editproses)
	btndelete.on("click",deleteproses)

	return app


justpy(Myapp)