import torch 
from transformers import MarianMTModel, MarianTokenizer

import tkinter as tk
from tkinter import ttk, messagebox

# Encapsulation: The concept of bundling data and methods that oprate on the data into a single unit or class, while rstricting access to some of the class's component is called Encapsulation.
# 'TranslatorApp' class encapsulates the methods and attributes of the app by following the concepts of Encapsulation

class TranslatorApp(tk.Tk):  # Inheritance : Inheritance is concept where a new class inherits attributes and methods from an existing class.
                             # 'TranslatorApp' inherits the window functionality from 'tk.TK'. 

                             
    def __init__(self):   # Overriding: Ovverriding is the concept of providing a new implementation of a method in the subclass , which is already defined in its superclass.
                          # '__init__' constructor method overrides the constructor of 'tk.TK' by changing the defination of '__init__'

        super().__init__()

        self.title("Translator App")
        self.geometry("1200x900")
        self.configure(bg='light grey')
 
        self.models = {
            'English to Spanish' : 'Helsinki-NLP/opus-mt-en-es',
            'Spanish to English' : 'Helsinki-NLP/opus-mt-es-en',
            'English to French' : 'Helsinki-NLP/opus-mt-en-fr',
            'French to English' : 'Helsinki-NLP/opus-mt-fr-en',
            'English to German' : 'Helsinki-NLP/opus-mt-en-de',
            'German to English' : 'Helsinki-NLP/opus-mt-de-en',
            'English to Russian' : 'Helsinki-NLP/opus-mt-en-ru',    
            'Russian to English' : 'Helsinki-NLP/opus-mt-ru-en',
            'English to Chinese' : 'Helsinki-NLP/opus-mt-en-zh',
            'Chinese to English' : 'Helsinki-NLP/opus-mt-zh-en',
            'English to Japanese' : 'Helsinki-NLP/opus-mt-en-ja',
            'Japanese to English' : 'Helsinki-NLP/opus-mt-ja-en',
            'English to Arabic' : 'Helsinki-NLP/opus-mt-en-ar',
            'Arabic to English' : 'Helsinki-NLP/opus-mt-ar-en',
            'English to Italian' : 'Helsinki-NLP/opus-mt-en-it',
            'Italian to English' : 'Helsinki-NLP/opus-mt-it-en',
            'English to Portuguese' : 'Helsinki-NLP/opus-mt-en-pt',
            'Portuguese to English' : 'Helsinki-NLP/opus-mt-pt-en',
            'English to Dutch' : 'Helsinki-NLP/opus-mt-en-nl',
            'Dutch to English' : 'Helsinki-NLP/opus-mt-nl-en',
            'English to Turkish' : 'Helsinki-NLP/opus-mt-en-tr',
            'Turkish to English' : 'Helsinki-NLP/opus-mt-tr-en',
            'English to Korean' : 'Helsinki-NLP/opus-mt-en-ko',
            'Korean to English' : 'Helsinki-NLP/opus-mt-ko-en',
            'English to Hindi' : 'Helsinki-NLP/opus-mt-en-hi',
            'Hindi to English' : 'Helsinki-NLP/opus-mt-hi-en',
            

        }

        self.current_modelname = 'Helsinki-NLP/opus-mt-en-es'
        self.tokenizer = MarianTokenizer.from_pretrained(self.current_modelname)
        self.model = MarianMTModel.from_pretrained(self.current_modelname)


        self.create_widget()



    def create_widget(self):
        # Header Frame
        self.header_frame = tk.Frame(self, bg="light grey")
        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.header_frame, text="AI Translator", font=("Arial", 26, "bold"), bg="light grey", fg="black")
        self.title_label.pack(pady=20)

        # Input Frame 
        self.input_frame = tk.Frame(self, bg="light grey")
        self.input_frame.pack(padx=20, pady=20, fill=tk.X)


        self.input_label = tk.Label(self.input_frame, text="Enter text to translate:", font=("Arial", 16), bg="light grey", anchor="w")
        self.input_label.pack(pady=10, fill = tk.X)

        self.input_text = tk.Text(self.input_frame, height=10, width=50,font=("Arial", 14))
        self.input_text.pack(pady=15, padx=15, fill=tk.X)

        #Translation Control Frame
        self.controls_frame = tk.Frame(self, bg="light grey")
        self.controls_frame.pack(padx=20, pady=10, fill=tk.X)

        self.language_label = tk.Label(self.controls_frame, text= "Select Translation:",font=("Arial", 16), bg="light grey", anchor="w")
        self.language_label.grid(row=0, column=0, padx=10, pady=10)

        self.lang_combox = ttk.Combobox(self.controls_frame, values= list(self.models.keys()), state="readonly", font=("Arial", 12))
        self.lang_combox.grid(row=0, column=1, padx=5, pady=5)

        self.lang_combox.current(0)
        self.lang_combox.bind("<<ComboboxSelected>>", self.change_model)

        self.translate_button = tk.Button(self.controls_frame, text= "Translate", command=self.translate_text, bg="red", fg="white", font=("Arial", 12, "bold"))
        self.translate_button.grid(row=0, column=2, padx=10, pady=5)

        #Output Frame

        self.output_frame = tk.Frame(self, bg="light grey")
        self.output_frame.pack(padx=20, pady=20, fill=tk.X)

        self.output_label = tk.Label(self.output_frame, text= "Translated text:",font=("Arial", 16), bg="light grey", anchor="w")
        self.output_label.pack(pady=10, fill=tk.X)

        self.output_text = tk.Text(self.output_frame, height=10, width=50,font=("Arial", 14))
        self.output_text.pack(pady=15,padx=15, fill=tk.X)
    
    def change_model(self, event= None):
        
        selected_lang_pair = self.lang_combox.get()
        self.current_modelname = self.models[selected_lang_pair]

        messagebox.showinfo("Model Loding", f"Model for {selected_lang_pair} is Loading!")

        self.tokenizer = MarianTokenizer.from_pretrained(self.current_modelname) 
        self.model = MarianMTModel.from_pretrained(self.current_modelname)          # Polymorphism: Polymorphism is a OOP concept where a method can behave differently based on the object's context.
                                                                                    # Both 'MarianTokenizer' and 'MarianMTModel' classes have methods with same name (e.g. 'from_pretrained()'), but these methods behaves differently depending on the chosen class.
                                                                                    

        messagebox.showinfo("Model Loaded", f"Model for {selected_lang_pair} loaded successfully!")

    def translate_text(self): # Abstraction: Abstraction is the process of hiding the implementation details and exposing only the essential features of an object. 
                              # The 'translate_text()' method abstracts the complexcity of how the translation model works.

        input_text =self.input_text.get("1.0",tk.END).strip()

        if not input_text:
            messagebox.showwarning("Empty Input", "Please enter some text to translate!")
            return
        
        inputs = self.tokenizer(input_text, return_tensors = "pt", padding = True)

        with torch.no_grad():
            translated_tooken = self.model.generate(**inputs)    # Polymorphism:  Polymorphism is a OOP concept where a method can behave differently based on the object's context.
                                                                 # The app can switch between various translation models using the same 'generate' method.
        
        translated_text = self.tokenizer.decode(translated_tooken[0], skip_special_tokens = True)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translated_text)

try:
    app = TranslatorApp()
    app.mainloop()
except Exception as e:
    print(f"Error:  {e}")
            