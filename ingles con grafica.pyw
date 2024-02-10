
from tkinter import *
from tkinter import messagebox
import tkinter as tk




root = tk.Tk()  # Crea una ventana
root.title("Tiempos verbales")  # Titulo de la ventana
root.iconbitmap("icono.ico")  # Icono de la ventana
# variables
varopcion = IntVar()  # Variable para el radiobutton
sino = IntVar()  # Variable para el radiobutton


frame = Frame(root)  # Crea un frame
frame.pack()  # Pone el frame en la ventana
frame.config(width="650", height="350", padx=80, pady=20)  # Configura el frame

cesarimg = PhotoImage(file="temp verbals.png")  # Imagen de la ventana


Label(frame, image=cesarimg).pack()  # Pone la imagen en el frame

messagebox.showinfo("Tiempos verbales", "Programa elaborado por Jorge") 


Label(frame, text="\n\nSeleccione un tiempo verbal:").pack()


Radiobutton(frame, text="Present Simple", variable=varopcion, value=0).pack()
Radiobutton(frame, text="Present continuous",
            variable=varopcion, value=2).pack()
Radiobutton(frame, text="Present perfect", variable=varopcion, value=3).pack()
Radiobutton(frame, text="Present perfect continuos",
            variable=varopcion, value=4).pack()


frame2 = Frame(frame)
frame2.pack()

label6 = Label(frame2, text="\n\nSeleccione un tipo de oración:",
               font=("Comic Sans", 9))
label6.grid(row=1, column=0, columnspan=3, sticky="we", padx=10, pady=10)


r1 = Radiobutton(frame2, text="Afirmative", variable=sino, value=0)
r2 = Radiobutton(frame2, text="Negative", variable=sino, value=2)
r3 = Radiobutton(frame2, text="Interrogative", variable=sino, value=3)
r1.grid(row=2, column=0, padx=50, pady=10)
r2.grid(row=2, column=1, padx=50, pady=10)
r3.grid(row=2, column=2, padx=50, pady=10)


def info():
    global varopcion
    global sino

    root1 = Toplevel()
    root1.title("Tiempos verbales")
    root1.iconbitmap("icono.ico")
    # variables
    yn = IntVar()
    sino1 = IntVar()
    fra3 = Frame(root1)
    fra3.pack()
    text = Text(fra3, width=120, height=30)
    text.pack()

    Label(root1, text="\n\n¡Desea crear un ejemplo?").pack()
    fral = Frame(root1)
    fral.pack()
    fral.config(width="650", height="350", padx=80, pady=20)

    def ejemplo():
        def generarora():
            global varopcion
            global sino
            sujec = sujeto.get()
            sujec = sujec.strip()
            sujec = sujec.lower()

            verb = verbo.get()
            verb = verb.strip()
            verb = verb.lower()

            comple = complemento.get()
            comple = comple.lower()

            if varopcion.get() == 0:
                if sujec == "she" or sujec == "he" or sujec == "it":
                    if verb[-1:] == "o" or verb[-1:] == "x" or verb[-1:] == "z":
                        transcripcion = verb + "es"

                    elif verb[-2:] == "sh" or verb[-2:] == "ch" or verb[-2:] == "ss":
                        transcripcion = verb + "es"

                    elif verb[-2:] == "ay" or verb[-2:] == "ey" or verb[-2:] == "iy" or verb[-2:] == "oy" or verb[-2:] == "uy":
                        transcripcion = verb + "s"

                    elif verb[-1:] == "y":
                        transcripcion = verb[:-1] + "ies"

                    else:
                        transcripcion = verb + "s"

                elif sujec == "they" or sujec == "we" or sujec == "you" or sujec == "i":
                    transcripcion = verb

                else:
                    messagebox.showwarning(
                        "Error", "No se puede generar un ejemplo, asegurese de escribir los sujetos he,she,it,i,they,you o we")

                txt.insert(END, "\n* * * * * * * * * * * * ")
                txt.insert(END, "\n* Oración afirmativa: *")

                txt.insert(END, f"\n\n*{sujec} + {transcripcion} + {comple}")
                txt.insert(END, "\n* * * * * * * * * * * * ")

                if sujec == "she" or sujec == "he" or sujec == "it":
                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + does + not + {verb} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                else:
                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + do + not + {verb} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                if sujec == "she" or sujec == "he" or sujec == "it":
                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n*does + {sujec} + {verb} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                else:
                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n*do + {sujec} + {verb} + {comple} + ? ")
                    txt.insert(END, "\n\n* * * * * * * * * * * *  *")

            elif varopcion.get() == 2:
                if sujec == "she" or sujec == "he" or sujec == "it" or sujec == "we" or sujec == "they" or sujec == "you" or sujec == "i":

                    if verb[-1:] == "y":
                        transcripcion = verb + "ing"

                    elif verb[-2:] == "ee":
                        transcripcion = verb + "ing"

                    elif (verb[-1:] != "a" or verb[-1:] != "e" or verb[-1:] != "i" or verb[-1:] != "o" or verb[-1:] != "u") and (verb[-2:-1] == "a" or verb[-2:-1] == "e" or verb[-2:-1] == "i" or verb[-2:-1] == "o" or verb[-2:-1] == "u"):
                        transcripcion = verb + verb[-1:] + "ing"

                    elif verb[-1:] == "e":
                        transcripcion = verb[:-1] + "ing"

                    elif verb[-2:] == "ye":
                        transcripcion = verb[:-2] + "ing"

                    else:
                        transcripcion = verb + "ing"

                else:
                    messagebox.showwarning(
                        "Error", "No se puede generar un ejemplo, asegurese de escribir los sujetos he,she,it,i,they,you o we")

                if sujec == "i":

                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + am + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + am + not + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n* am + {sujec}  + {transcripcion} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                elif sujec == "she" or sujec == "he" or sujec == "it":

                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + is + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + is + not + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n*is + {sujec}  + {transcripcion} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                elif sujec == "they" or sujec == "we" or sujec == "you":
                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(
                        END, f"\n\nn{sujec} + are + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + are + not + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n* are + {sujec}  + {transcripcion} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                else:
                    messagebox.showwarning(
                        "Error", "No se puede generar un ejemplo, asegurese de escribir los sujetos he,she,it,i,they,you o we")

            elif varopcion.get() == 3:
                if sujec == "i" or sujec == "you" or sujec == "we" or sujec == "they":

                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(END, f"\n\n*{sujec} + have + {verb} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(END, f"\n\n*{sujec}'ve + {verb} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + have + not + {verb} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(
                        END, f"\n\n*{sujec} + haven't + {verb} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n* have + {sujec}  + {verb} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                elif sujec == "she" or sujec == "he" or sujec == "it":

                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(END, f"\n\n*{sujec} + has + {verb} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(END, f"\n\n*{sujec}'s + {verb} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + has + not + {verb} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(
                        END, f"\n\n*{sujec} + hasn't + {verb} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n* has + {sujec}  + {verb} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                else:
                    messagebox.showwarning(
                        "Error", "No se puede generar un ejemplo, asegurese de escribir los sujetos he,she,it,i,they,you o we")

            elif varopcion.get() == 4:
                if sujec == "she" or sujec == "he" or sujec == "it" or sujec == "we" or sujec == "they" or sujec == "you" or sujec == "i":

                    if verb[-1:] == "y":
                        transcripcion = verb + "ing"

                    elif verb[-2:] == "ee":
                        transcripcion = verb + "ing"

                    elif (verb[-1:] != "a" or verb[-1:] != "e" or verb[-1:] != "i" or verb[-1:] != "o" or verb[-1:] != "u") and (verb[-2:-1] == "a" or verb[-2:-1] == "e" or verb[-2:-1] == "i" or verb[-2:-1] == "o" or verb[-2:-1] == "u"):
                        transcripcion = verb + verb[-1:] + "ing"

                    elif verb[-1:] == "e":
                        transcripcion = verb[:-1] + "ing"

                    elif verb[-2:] == "ye":
                        transcripcion = verb[:-2] + "ing"

                    else:
                        transcripcion = verb + "ing"

                else:
                    messagebox.showwarning(
                        "Error", "No se puede generar un ejemplo, asegurese de escribir los sujetos he,she,it,i,they,you o we")

                if sujec == "i" or sujec == "they" or sujec == "we" or sujec == "you":

                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + have + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(
                        END, f"\n\n*{sujec}'ve + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + have + not + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(
                        END, f"\n\n*{sujec} + haven't + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n* have + {sujec}  + been + {transcripcion} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")

                elif sujec == "she" or sujec == "he" or sujec == "it":

                    txt.insert(END, "\n* * * * * * * * * * * * ")
                    txt.insert(END, "\n* Oración afirmativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + has + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(
                        END, f"\n\n*{sujec}'s + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * * * ")

                    txt.insert(END, "\n\n\n* * * * * * * * * * *")
                    txt.insert(END, "\n* Oración negativa: *")
                    txt.insert(
                        END, f"\n\n*{sujec} + has + not + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n\nor")
                    txt.insert(
                        END, f"\n\n*{sujec} + hasn't + been + {transcripcion} + {comple}")
                    txt.insert(END, "\n* * * * * * * * * * *")

                    txt.insert(END, "\n\n\n* * * * * * * * * * * *  *")
                    txt.insert(END, "\n* Oración interrogativa: *")
                    txt.insert(
                        END, f"\n\n* has + {sujec}  + been + {transcripcion} + {comple} + ?")
                    txt.insert(END, "\n* * * * * * * * * * * *  *")
                else:
                    messagebox.showwarning(
                        "Error", "No se puede generar un ejemplo, asegurese de escribir los sujetos he,she,it,i,they,you o we")

        global varopcion
        global sino

        if yn.get() == 0:
            def clear_text():
                txt.delete("1.0", "end")
                verbo.delete(0, END)
                sujeto.delete(0, END)
                complemento.delete(0, END)

            root2 = Toplevel()
            root2.title("Generar Oración")
            root2.iconbitmap("icono.ico")
            f = Frame(root2)
            f.pack()
            f.config(width="150", height="100", padx=80, pady=20)
            sujetol = Label(f, text="Enter the subject:",
                            font=("Comic Sans", 9))
            sujetol.grid(row=0, column=0, sticky="w")
            sujeto = Entry(f)
            sujeto.grid(row=0, column=1, sticky="w")

            if varopcion.get() == 0:
                verbol = Label(f, text="Enter the verb infinitive:",
                               font=("Comic Sans", 9))
            elif varopcion.get() == 2:
                verbol = Label(f, text="Enter the infinitive verb and that does not belong to the stative verbs:",
                               font=("Comic Sans", 9))

            elif varopcion.get() == 3:
                verbol = Label(f, text="Enter the participle of verb: ",
                               font=("Comic Sans", 9))
            elif varopcion.get() == 4:
                verbol = Label(f, text="Enter the infinitive verb and that does not belong to the stative verbs:  ",
                               font=("Comic Sans", 9))

            verbol.grid(row=1, column=0, sticky="w")
            verbo = Entry(f)
            verbo.grid(row=1, column=1, sticky="w")

            complementol = Label(f, text="Enter the complement: ",
                                 font=("Comic Sans", 9))
            complementol.grid(row=2, column=0, sticky="w")
            complemento = Entry(f)
            complemento.grid(row=2, column=1, rowspan=2,
                             columnspan=2, sticky="w")

            Bot = Button(f, text="Generar oración", command=generarora)
            Bot.grid(row=4, column=1, sticky="w")

            fr = Frame(root2)
            fr.pack()
            Label(fr, text="Oración:", font=("Comic Sans", 14)).pack()
            txt = Text(fr, width=80, height=24)
            txt.pack()

            fo = Frame(root2)
            fo.pack()
            but = Button(fo, text="Limpiar", command=clear_text)
            but.grid(row=0, column=1, sticky="w")
            sal = Button(fo, text="Salir", command=root2.destroy)
            sal.grid(row=0, column=2, sticky="w")

        elif yn.get() == 2:
            root1.destroy()

    yes = Radiobutton(fral, text="SI", variable=yn, value=0)
    no = Radiobutton(fral, text="NO", variable=yn, value=2)
    yes.grid(row=3, column=1)
    no.grid(row=3, column=2)
    Boton = Button(root1, text="Continuar", command=ejemplo)
    Boton.pack()

    if varopcion.get() == 0:
        if sino.get() == 0:
            text.insert(
                END, "\nPara formar una oración afirmativa en presente simple, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(END, "\n\n\nSUJETO + VERBO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, thent, one verb, and finally, one complement, now, for write the sentence you must put the subjcet at the beginning of the sentence, then, the infinitive verb, but, must to having in mind some rules if you think work with third person :")
            text.insert(END, "\n\n\n1. The verb must be in infinitive form.")
            text.insert(END, "\n\n2. Add -s to the end of the verb, but if, the verbo finshes with '-ss, -sh, -ch, -o, -x or -z', then, you must add '-es' to the end of the verb in the third person singular.")
            text.insert(
                END, "\n\n3. On the other hand if, the verb finshes with 'consonant and y', then, you must add '-ies' to the end of the verb, replacing the 'y'.")
            text.insert(
                END, "\n\n4. In case, of that the verb finshes with '-e', then, you must add '-es' to the end of the verb.")
            text.insert(
                END, "\n\n5. but if, the verb finshes witn 'vocal + y',then, you must keep the 'y' and add '-s' to the end of the verb.")

            text.insert(
                END, "\n\n\n\nFinally if, you not think work with third person, then, must skip all previous.")

            text.insert(
                END, "\nLast but not least, if wast write one complement, this must go the final of the sentence.")
            text.insert(
                END, "\n\nExamples : \n-- She works from home\n-- I go to church on Sundays\n")

        elif sino.get() == 2:

            text.insert(
                END, "\nPara formar una oración negativa en presente simple, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + AUXILIAR “DO” o “DOES” + NOT + VERBO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, then one verb, and finally, one complement, now, for write the sentence you must put the subject at the beginning of the sentence, then, the auxiliary “DO” or “DOES”, however for know when to use do or does, you must to having in mind some indications  :")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must of write “does” instead of “do” regardless of the verb.")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “do” instead of “does” regardless of the verb.")

            text.insert(END, "\n\n\n Now, must continue the negation (not), that may be used in a contraction or only.In contracction “DOES NOT” is remplaced by  “DOESN't” and “DO NOT” is remplaced by “DON'T”.")
            text.insert(END, "\nAfter, you must write the verb infinitive.")

            text.insert(
                END, "\nLast but not least if, wast write one complement, this must go the final of the sentence.")
            text.insert(END, "\n\nExamples : \n-- He does not live in Boston or He doesn’t live in Boston\n-- We do not go to the movies every weekend or We don’t go to the movies every weekend.\n")

        elif sino.get() == 3:
            text.insert(
                END, "\nPara formar una oración interrogativa en presente simple, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\n AUXILIAR “DO” o “DOES” + SUJETO + VERBO + COMPLEMENTO + ?")

            text.insert(END, "\n\n\nFirst, you have to think one subject, then, one verb, and finally, one complement, now, for write the sentence you must put the auxiliary “DO” o “DOES”  at the beginning of the sentence, then, the subject, however for know when to use do or does, you must to having in mind some indications  :")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must of write “does” instead of “do” regardless of the verb.")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “do” instead of “does” regardless of the verb.")

            text.insert(END, "\n\n\nAfter, you must write the verb infinitive.")

            text.insert(
                END, "\nLast but not least if, wast write one complement, this must go the final of the sentence.")
            text.insert(END, "\n\nExamples : \n-- He does not live in Boston or He doesn’t live in Boston\n-- We do not go to the movies every weekend or We don’t go to the movies every weekend\n")

    elif varopcion.get() == 2:

        if sino.get() == 0:

            text.insert(
                END, "\nPara formar una oración afirmativa en presente continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + VERBO TO BE + VERBO CON GERUNDIO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, then, one verb to be, next, a verb and finally, one complement, now, for write the sentence you must put the subjcet at the beginning of the sentence, then, the verb to be, but, must to having in mind some rules for that:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “is” regardless of the verb")
            text.insert(
                END, "\n\n2. If, the subject is “you”, so you must write “are” regardless of the verb")
            text.insert(
                END, "\n\n3. in case, of that the subject is “I”, so you must write “am” regardless of the verb")
            text.insert(
                END, "\n\n4. Otherwise if, the subject is plural, then you must write “are” regardless of the verb")

            text.insert(
                END, "\n\n\n\nNow, you must write the verb gerundio, but, for that you must to having in mind some rules:")

            text.insert(END, "\n\n\n1. All the verbs must finish with “ING”")
            text.insert(END, "\n\n2. Second if verb has a single syllable or whose accent falls on the last syllable and ends in a consonant, the latter must be doubled and “-ING” must be added to the end of the verb")
            text.insert(
                END, "\n\n3. In case, of that the verb finshes in an -e that is not pronounced, instead go “e” must go “ing”")
            text.insert(
                END, "\n\n4. On the other hand if, the verb finshes with “ee” Not only must stay the “ee” but, also must add “ing” to the end of the verb")

            text.insert(
                END, "\n\n5. Finally if, one verb finshes witn “ie”, these lyrics must be replaced by “y” and the “ing” must be added to the end of the verb")

            text.insert(
                END, "\n\n\nLast but not least if, wast write one complement, this must go the final of the sentence")
            text.insert(
                END, "\n\nExamples : \n-- I am running every morning\n-- He is working at the cinema\n-- He is dating a friend of my sister\n")

        elif sino.get() == 2:

            text.insert(
                END, "\nPara formar una oración negativa en presente continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + VERBO TO BE + NOT + VERBO CON GERUNDIO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, thent, one verb to be, next, a verb and finally, one complement, now, for write the sentence you must put the subjcet at the beginning of the sentence, then, the verb to be, but, must to having in mind some rules for that:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “is” regardless of the verb")
            text.insert(
                END, "\n\n2. If, the subject is “you”, so you must write “are” regardless of the verb")
            text.insert(
                END, "\n\n3. in case, of that the subject is “I”, so you must write “am” regardless of the verb")
            text.insert(
                END, "\n\n4. Otherwise if, the subject is plural, then you must write “are” regardless of the verb")

            text.insert(
                END, "\n\n\n\nThen of that, you must add the “NOT” the sentence")

            text.insert(
                END, "\n\nNow, you must write the verb gerundio, but for that you must to having in mind some rules:")

            text.insert(END, "\n\n\n1. All yhe verbs must finish with “ING”")
            text.insert(END, "\n\n2. Second if, verb has a single syllable or whose accent falls on the last syllable and ends in a consonant, the latter must be doubled and “-ING” must be added to the end of the verb")
            text.insert(
                END, "\n\n3. In case, of that the verb finshes in an -e that is not pronounced, instead go “e” must go “ing”")
            text.insert(
                END, "\n\n4. On the other hand if, the verb finshes with “ee” Not only must stay the “ee” but also must add “ing” to the end of the verb")

            text.insert(
                END, "\n\n5. Finally if, one verb finshes witn “ie”, these lyrics must be replaced by “y” and the “ing” must be added to the end of the verb")

            text.insert(
                END, "\n\n\nLast but not least if, wast write one complement, this must go the final of the sentence")
            text.insert(
                END, "\n\nExamples : \n-- She is not crying for you\n-- We are not cutting the budget\n-- You are not taking it seriously\n")

        elif sino.get() == 3:

            text.insert(
                END, "\nPara formar una oración afirmativa en presente continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\n VERBO TO BE + SUJETO + VERBO CON GERUNDIO  + COMPLEMENTO + ?")

            text.insert(END, "\n\n\nFirst, you have to think one verb to be, thent, one subject, next, a verb and finally, one complement, now, for write the sentence you must put the verb to be at the beginning of the sentence, but, for that you must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “is” regardless of the verb")
            text.insert(
                END, "\n\n2. I,f the subject is “you”, so you must write “are” regardless of the verb")
            text.insert(
                END, "\n\n3. in case, of that the subject is “I”, so you must write “am” regardless of the verb")
            text.insert(
                END, "\n\n4. Otherwise if, the subject is plural, then you must write “are” regardless of the verb")

            text.insert(
                END, "\n\n\n\nThen of that, you must add the subject of the sentence, this should already be defined in her mind from the start.")

            text.insert(
                END, "\n\nNow, you must write the verb gerundio, but for that you must to having in mind some rules:")

            text.insert(END, "\n\n\n1. All yhe verbs must finish with “ING”")
            text.insert(END, "\n\n2. Second if, verb has a single syllable or whose accent falls on the last syllable and ends in a consonant, the latter must be doubled and “-ING” must be added to the end of the verb")
            text.insert(
                END, "\n\n3. In case, of that the verb finshes in an -e that is not pronounced, instead go “e” must go “ing”")
            text.insert(
                END, "\n\n4. On the other hand if, the verb finshes with “ee” Not only must stay the “ee” but also must add “ing” to the end of the verb")

            text.insert(
                END, "\n\n5. Finally if, one verb finshes witn “ie”, these lyrics must be replaced by “y” and the “ing” must be added to the end of the verb")

            text.insert(
                END, "\n\n\nLast but not least if, wast write one complement, this must go the final of the sentence")
            text.insert(
                END, "\n\nExamples : \n-- Are they playing hide and seek? \n-- Are you swimming with them?\n-- Is he riding a donkey? \n")

    elif varopcion.get() == 3:
        if sino.get() == 0:

            text.insert(
                END, "\nPara formar una oración afirmativa en presente continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + AUXILIAR “HAVE” O “HAS” + VERBO EN PARTICIPIO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, thent, one verb in participio and finally, one complement, now, for write the sentence you must put the subject at the beginning of the sentence, then, the auxiliary, but, for that must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “HAS” instead of “HAVE” regardless of the verb")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “have” instead of “has” regardless of the verb")

            text.insert(
                END, "\n\n\n\nNow, you must write the verb in participe and finally a complement if you want")
            text.insert(
                END, "\n\nExamples : \n-- I have/ I've been in Italy\n-- He/She has looked for	a new apartment\n-- We/We've have found the test result\n")

            text.insert(
                END, "\n\n\nIf you want to use contractions you may use them of the following way: ")
            text.insert(
                END, "\n\nI have = I’ve \nYou have = You’ve \nHe has = He’s\nShe has = She’s\nIt has = It’s\nWe have = We’ve\nThey	have =They’ve")

        elif sino.get() == 2:

            text.insert(
                END, "\nPara formar una oración negativa en presente continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + AUXILIAR “HAVE” O “HAS” + NOT + VERBO EN PARTICIPIO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, then, one verb in participio and finally, one complement, now, for write the sentence you must put the subject at the beginning of the sentence, then, the auxiliary, but, for that must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “HAS” instead of “HAVE” regardless of the verb")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “have” instead of “has” regardless of the verb")

            text.insert(
                END, "\n\n\n\nThen of that, you must add the “NOT” the sentence")

            text.insert(
                END, "\n\nNow, you must write the verb in participe and finally a complement if you want")
            text.insert(
                END, "\n\nExamples : \n-- I have not	been in Italy\n-- He/She has not looked for	a new apartment\n-- We have not found the test result\n")

            text.insert(
                END, "\n\n\n\nIf, you want to use contractions you may use them of the following way: ")
            text.insert(END, "\n\nI have = I haven't \nYou have = You haven't \nHe has = He hasn't\nShe has = she hasn't\nIt has = It haven't\nWe have = We haven't\nThey	have =They haven't")

        elif sino.get() == 3:
            text.insert(
                END, "\nPara formar una oración afirmativa en presente continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nAUXILIAR “HAVE” O “HAS” + SUJETO + VERBO EN PARTICIPIO + COMPLEMENTO +?")

            text.insert(END, "\n\n\nFirst, you have to think one subject, then, one verb in participio and finally, one complement, now, for write the sentence you must put the auxiliary at the beginning of the sentence, then, the subject, but, for that must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “HAS” instead of “HAVE” regardless of the verb")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “have” instead of “has” regardless of the verb")

            text.insert(
                END, "\n\n\n\nNow, you must write the verb in participe and finally a complement if you want")
            text.insert(
                END, "\n\nExamples : \n-- Have I been in Italy?\n-- Has he/she looked for a new apartment?\n-- Have we found the test result?\n")

    elif varopcion.get() == 4:
        if sino.get() == 0:
            text.insert(
                END, "\nPara formar una oración afirmativa en presente perfecto continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + AUXILIAR “HAVE” O “HAS” + BEEN + VERBO CON GERUNDIO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, then, one verb, and finally, one complement, now, for write the sentence you must put the subject at the beginning of the sentence, then, the auxiliary, but, for that must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “HAS” instead of “HAVE” regardless of the verb")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “have” instead of “has” regardless of the verb")

            text.insert(
                END, "\n\n\n\nThen of that, you must add the “BEEN” the sentence")

            text.insert(
                END, "\n\nNow, you must write the verb with gerundio, but, for that you must to having in mind some rules:")

            text.insert(END, "\n\n\n1. All yhe verbs must finish with “ING”")
            text.insert(END, "\n\n2. Second if, verb has a single syllable or whose accent falls on the last syllable and ends in a consonant, the latter must be doubled and “-ING” must be added to the end of the verb")
            text.insert(
                END, "\n\n3. In case, of that the verb finshes in an -e that is not pronounced, instead go “e” must go “ing”")
            text.insert(
                END, "\n\n4. On the other hand if, the verb finshes with “ee” Not only must stay the “ee” but, also must add “ing” to the end of the verb")
            text.insert(
                END, "\n\n5. Finally if, one verb finshes witn “ie”, these lyrics must be replaced by “y” and the “ing” must be added to the end of the verb")

            text.insert(
                END, "\n\n\n\nLast but not least if, wast write one complement, this must go the final of the sentence")
            text.insert(
                END, "\n\nExamples : \n-- I'm thirsty. I have been running.\n-- Maria has sunburns. She has been taking the sun the whole morning.\n")

            text.insert(
                END, "\n\n\nIf you want to use contractions you may use them of the following way: ")
            text.insert(
                END, "\nI have = I’ve \nYou have = You’ve \nHe has = He’s\nShe has = She’s\nIt has = It’s\nWe have = We’ve\nThey	have =They’ve")

        elif sino.get() == 2:
            text.insert(
                END, "\nPara formar una oración negativa en presente perfecto continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nSUJETO + AUXILIAR “HAVE” O “HAS” + NOT + BEEN + VERBO CON GERUNDIO + COMPLEMENTO")

            text.insert(END, "\n\n\nFirst, you have to think one subject, thent, one verb, and finally, one complement, now, for write the sentence you must put the subject at the beginning of the sentence, then, the auxiliary, but, for that must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “HAS” instead of “HAVE” regardless of the verb")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “have” instead of “has” regardless of the verb")

            text.insert(
                END, "\n\n\n\nNext, you must add the “NOT” the sentence and then the “BEEN”")

            text.insert(
                END, "\n\nNow, you must write the verb with gerundio, but, for that you must to having in mind some rules:")

            text.insert(END, "\n\n\n\n1. All the verbs must finish with “ING”")
            text.insert(END, "\n\n2. Second if, verb has a single syllable or whose accent falls on the last syllable and ends in a consonant, the latter must be doubled and “-ING” must be added to the end of the verb")
            text.insert(
                END, "\n\n3. In case, of that the verb finshes in an -e that is not pronounced, instead go “e” must go “ing”")
            text.insert(
                END, "\n\n4. On the other hand if, the verb finshes with “ee” Not only must stay the “ee” but, also must add “ing” to the end of the verb")
            text.insert(
                END, "\n\n5. Finally if, one verb finshes witn “ie”, these lyrics must be replaced by “y” and the “ing” must be added to the end of the verb")

            text.insert(
                END, "\n\n\n\nLast but not least if, wast write one complement, this must go the final of the sentence")
            text.insert(
                END, "\n\nExamples : \n-- He has not been eating well. \n-- They haven't been working together.\n")

            text.insert(
                END, "\n\n\nIf you want to use contractions you may use them of the following way: ")
            text.insert(
                END, "\nI have = I’ve \nYou have = You’ve \nHe has = He’s\nShe has = She’s\nIt has = It’s\nWe have = We’ve\nThey	have =They’ve")

        elif sino.get() == 3:

            text.insert(
                END, "\nPara formar una oración afirmativa en presente perfecto continuo, se debe utilizar la siguiente sintaxis e indicaciones:")
            text.insert(
                END, "\n\n\nAUXILIAR “HAVE” O “HAS” + SUJETO + BEEN + VERBO CON GERUNDIO + COMPLEMENTO +?")

            text.insert(END, "\n\n\nFirst, you have to think one subject, thent, one verb,and finally, one complement, now, for write the sentence you must put the auxiliary at the beginning of the sentence, then, the subject, but, for that must to having in mind some rules:")
            text.insert(
                END, "\n\n\n1. In case, of that the subject be third person, you must must of write “HAS” instead of “HAVE” regardless of the verb")
            text.insert(
                END, "\n\n2. On the contrary if, el subject not be third person, you must write “have” instead of “has” regardless of the verb")

            text.insert(
                END, "\n\n\n\nThen of that, you must add the “BEEN” the sentence")

            text.insert(
                END, "\n\nNow, you must write the verb with gerundio, but, for that you must to having in mind some rules:")

            text.insert(END, "\n\n\n1. All yhe verbs must finish with “ING”")
            text.insert(END, "\n\n2. Second if ,verb has a single syllable or whose accent falls on the last syllable and ends in a consonant, the latter must be doubled and “-ING” must be added to the end of the verb")
            text.insert(
                END, "\n\n3. In case, of that the verb finshes in an -e that is not pronounced, instead go “e” must go “ing”")
            text.insert(
                END, "\n\n4. On the other hand if, the verb finshes with “ee” Not only must stay the “ee” but, also must add “ing” to the end of the verb")
            text.insert(
                END, "\n\n5. Finally if, one verb finshes witn “ie”, these lyrics must be replaced by “y” and the “ing” must be added to the end of the verb")

            text.insert(
                END, "\n\n\n\nLast but not least if, wast write one complement, this must go the final of the sentence")
            text.insert(
                END, "\n\nExamples : \n-- Has she been training?. \n-- How long have we been cooking?.\n")

            text.insert(
                END, "\n\n\nIf you want to use contractions you may use them of the following way: ")
            text.insert(
                END, "\nI have = I’ve \nYou have = You’ve \nHe has = He’s\nShe has = She’s\nIt has = It’s\nWe have = We’ve\nThey	have =They’ve")


Boton = Button(root, text="Generar Información", command=info)
Boton.pack()


root.mainloop()
