"""
File met objecten die fungeren als interface tussen de verschillende lagen van de automatisering.
"""
from typing import List


class TransformationInputInterface:
    columns: List[str] = [
        'CallId',
        'Segment',  
        'Start',
        'Stop',
        'Calling Party',
        'Trunk Group',
        'Dialed Number',   
        'Answered Agent',  
        'Original Agent',
        'Call Disposition', 
        'Vector',        
        'Priority',
        'Split',  
        'Level', 
        'System',
        'Queue',   
        'Ring',   
        'Talk',
        'Hold',    
        'ACW',
        'Consult',
        'Disposition',        
        'Duration',                  
        1,
        2,                  
        3,                  
        4,
        5,                  
        6,                  
        7,
        8,                  
        9,    
        '1.1',
        '2.1',    
        '3.1',    
        '4.1',
        '5.1'
    ]


class ReportDatasetInterface:
    columns: List[str] = [
        "Gemiddelde Antwoord Snelheid",
        "Gemiddelde Annuleer-tijd",
        "Aangeboden",
        "ACD-Oproepen",
        "Gemiddelde ACD-tijd",
        "Gemiddelde ACW-tijd",
        "Geannuleerde Oproepen",
        "Maximale Vertraging",
        "Maximale In-wachtrij",
        "Extensie Uit-gesprek",
        "Gemiddelde Extensie Uit-gesprek",
        "ACD-Tijd (%)",
        "Beantwoorde Oproepen (%)",
        "Binnen Service-Level (%)",
        "Omgeleid Geen Antwoord"
    ]