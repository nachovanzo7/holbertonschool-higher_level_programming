#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    try:
        if not isinstance(template, str) or not isinstance(attendees, list):
            raise TypeError("The template should be a String and attendees a dictionary")

        if template == None:
            raise ValueError("Template is empty, no output files generated.")

        if attendees == None or len(attendees) == 0:
            raise ValueError("No data provided, no output files generated.")

        i = 1
        for x in attendees:
            
            texto = template.format(
                name=x.get("name", "N/A"),
                event_title=x.get("event_title", "N/A"),
                event_date=x.get("event_date", "N/A"),
                event_location=x.get("event_location", "N/A")
            )
                    
            with open("output_{}.txt".format(i), "w") as warchivo:
                warchivo.write(texto)
                    
            i += 1
            
        print("Se creo con exito")
                    
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)