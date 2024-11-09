#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str) or not isinstance(attendees, list):
            raise TypeError

        if template == None:
            raise ValueError("Template is empty, no output files generated.")

        if attendees == None:
            raise ValueError("No data provided, no output files generated.")


        i = 1
        for x in attendees:
            if os.path.exists(template):
                with open(template, "r") as archivo:
                    texto = archivo.read().format(
                    x.get("name", "N/A"),
                    x.get("event_title", "N/A"),
                    x.get("event_date", "N/A"),
                    x.get("event_location", "N/A")
                )
                        
                with open("output_{}.txt".format(i), "w") as warchivo:
                    warchivo.write(texto)
                    
            i += 1
        print("Se creo con exito")
                    
    except TypeError:
        print("The template should be a String and attendees a dictionary")