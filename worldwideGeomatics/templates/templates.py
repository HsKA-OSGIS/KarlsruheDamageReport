# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

import worldwide.wwfunctions
import os

dir_base=os.path.dirname(__file__) #path to current file

def create_head():
    """
    The document starts and creates the head
    """
    file_name=dir_base+"/html_sections/head.html"
    head=worldwide.wwfunctions.read_file(file_name)
    
    return head

def create_header():
    """
    Starts the body and creates the main menu
    """
    file_name=dir_base+"/html_sections/header.html"
    header=worldwide.wwfunctions.read_file(file_name)
    
    return header

def create_map():
    """
    Creates the map
    """
    file_name=dir_base+"/html_sections/map.html"
    map_sec=worldwide.wwfunctions.read_file(file_name)
    
    return map_sec

def create_table():
    """
    Creates the table
    """
    file_name=dir_base+"/html_sections/table.html"
    table=worldwide.wwfunctions.read_file(file_name)
    
    return table

def create_aside():
    """
    Creates the lateral menu
    """
    file_name=dir_base+"/html_sections/aside.html"
    aside=worldwide.wwfunctions.read_file(file_name)
    
    return aside

def create_footer():
    """
    Creates the footer and finishes the html
    """
    file_name=dir_base+"/html_sections/footer.html"
    footer=worldwide.wwfunctions.read_file(file_name)
    
    return footer

def start_general_section():
    """
    Starts general section
    """
    html='<section id="general_section">'
    
    return html

def close_general_section():
    """
    Closes general section
    """
    html='</section>'
    
    return html

def create_complete_page(draw_map=False, draw_table=False, html_ins=None):
    """
    Creates a web page with all of its parts and allows changing the content
    of the main section giving the html code and allows to visualize or not 
    the map and the table.

    Parameters:
    * draw_map: if it's true, it will creates openlayers map section
    * draw_table: if it's true, it will creates the table
    * html_ins: html code
    """
    #pydevd.settrace()

    head=create_head()
    header=create_header()
    start_general=start_general_section()
    
    if draw_map:
        map_sec=create_map()
    else:
        map_sec=""
        
    if draw_table:
        table=create_table()
    else:
        table=""
        
    if html_ins <> None:
        section=html_ins
    else:
        section=""
        
    close_general=close_general_section()
    aside=create_aside()
    footer=create_footer()
    html=head+header+map_sec+start_general+section+table+close_general+aside+footer 
    return html