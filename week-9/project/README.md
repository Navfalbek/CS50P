# Weather app
    #### Video Demo:  <https://youtu.be/7ROg_eeMvNU>
    #### Description:
    A simple weather app created in python programming language using 'tkinter', 'customtkinter', 'json' and 'requests' libraries. 
    Backend of the program connected to openweathermap.org web page and this program gets all informations from there. There used simple UI
    that user never get lost :). You just enter your city name that you want to know weather and that's it shows the weather in 'celsius' 
    and 'fahrenheits'. If the  user entered non-existent city name it's shows an error window which asks from user to enter it agian. 
    Next time you go outside just take a look to the weather and you never catch cold :). The working principle of the project is simple. 
    Main function calls gui function which contains all gui of the project. Than gui function calls search function which calls get_coordinates 
    function find latitude and longitude of the entered city by the user. The reason of doing that was openweathermap.org web pages api doc only 
    recieves latitude and longitude. And than according to the coordinates it finds the corresponding city. Finally, get_wetaher function recieves 
    json from get_coordinates and then find corresponding informations from it and sends it to the gui function. That's it, Thank you.
