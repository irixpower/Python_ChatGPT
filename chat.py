from tkinter import *
import customtkinter
import openai
import os
import pickle


root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x430')
root.iconbitmap('ai_lt.ico')
# Set colour Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Submit to ChatGPT
def speak():
    if chat_entry.get():
        # Define filename for API-key
        filename = "api_key"
        try:
            if os.path.isfile(filename):
                # Open the API-key-file
                input_file = open(filename, 'rb')

                # Load data from 
                stuff = pickle.load(input_file)

                # Query ChatGPT
                #Define our API-ket to ChatGPT
                openai.api_key = stuff

                # Create an instance

                openai.Model.list()

                # Define our query / response

                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=chat_entry.get(),
                    temperature=0,
                    max_tokens=60,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )

                my_text.insert(END, (response["choices"][0]["text"]).strip())
                my_text.insert(END, "\n\n")

            else:
                # Cretate the file
                input_file = open(filename, 'wb')
                # Close the file
                input_file.close()
                # Error message you need an API-key
                my_text.insert(END, "\n\nYou need an API-key to query ChatGPT\n\n")

        except Exception as e:
            my_text.insert(END, f"\n\n There was an error \n\n{e}")

        # Do Something
        pass
    else:
        my_text.insert(END, "\n\nYou haven't provided any input")


# Clear screen
def clear():
	# Clear the main text box
	my_text.delete(1.0, END)
	# Clear the query
	chat_entry.delete(0, END)

# Do API stuff
def key():
	
	
	# Define filename for API-key
	filename = "api_key"

	try:

		if os.path.isfile(filename):
			# Open the API-key-file
			input_file = open(filename, 'rb')

			# Load data from 
			stuff = pickle.load(input_file)

			# Clear the API entry widget
			api_entry.delete(0, END)

			# Output stuff to our entry box
			api_entry.insert(END, stuff)
		else:
			# Cretate the file
			input_file = open(filename, 'wb')
			# Close the file
			input_file.close()

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error \n\n{e}")

	# Resize App larger
	root.geometry('600x550')
	# Show API frame
	api_frame.pack(pady=25)

# Save the API key
def save_key():
	# Define the file name for the API-key
	filename = "api_key"

	try:

		# Open file
		output_file = open(filename, 'wb')

		# Add data to file
		pickle.dump(api_entry.get(), output_file)

		api_entry.delete(0, END)

		root.geometry('600x430')
		# Hide API Frame
		api_frame.pack_forget()
		# Resize app smaller
		root.geometry('600x430')

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error \n\n{e}")	

# Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

# Add Text Widget to get ChatGPT responses
my_text = Text(text_frame,
	bg="#343638",
	width=100,
	bd=1,
	fg="#6d6d6d",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")

my_text.grid(row=0, column=0)

# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

# Add the scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)

# Entry Widget to type stuff to ChatGPT
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Ask ChatGPT something",
	width=525,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

# Create Button Frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# Create submitt button
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak to ChatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

# Create clear button
clear_button = customtkinter.CTkButton(button_frame,
	text="Clear Screen",
	command=clear)
clear_button.grid(row=0, column=1, padx=35)

# Create API button
api_button = customtkinter.CTkButton(button_frame,
	text="Update API key",
	command=key)
api_button.grid(row=0, column=2, padx=25)

# Add API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=10)

# Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enterp API key",
	width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

#Add API button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)





root.mainloop()
