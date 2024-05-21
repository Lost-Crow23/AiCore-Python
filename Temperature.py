class Temperature:
    """
    This class is used to represent a date.
     
    Attribute:
        temp celcius(int): Temperature in celcius 

    """
    def __init__(self, temp_celsius):
        '''
        See help(Temperature) for accurate signature
        '''
        self.temp_celsius = temp_celsius

    def convert_temp_to_fahrenheit(self):
        '''
        This function returns the conversion from temperature in celcius to fahrenheit

        Returns:

            int: the integer representation of fahrenheit

        '''
        return (self.temp_celsius * 1.8) + 32

    @staticmethod
    def convert_fahrenheit_to_cel(temp_fah):
        '''
        This function is used for the conversion from fahrenheit to celcius.

        Returns:
            int: the integer representation of the temperature celcius.

        '''
        return (temp_fah - 32) * 1.8

    @staticmethod
    def check_valid_temp(temp):
        '''
        This function is used to ehck if the temperature is valid.

        Args: temperature (int): Temperature 

        Returns: 
            bool: true if the temperature is valid; False otherwise.
        '''
        if -273 <= temp <= 3000:
            print("This is a valid temperature")

    @classmethod
    def create_with_fahrenheit(cls, temperature):
        '''
        This function is used to create a temperature from the integer.

        Args:
            temperature (int): the integer representation of the temperature

        Returns: 
            Temperature (int): the integer representation of the temperature. 
        '''
        return cls(Temperature.convert_fahrenheit_to_cel(temperature))

    @classmethod
    def standard(cls):
        return cls(0)

    def __repr__(self) -> str:
        temp = str(self.temp_celsius)
        return temp
    
