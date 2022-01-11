"""
Test
"""

import unittest
import requests
import json
import time

from abc import ABC, abstractmethod

class test_weather_app(unittest.TestCase):
	"""Test the first method of the weather app."""

	def setUp(self):
		"""Set up test fixtures."""
		pass

	def test_get_results(self):
		"""Test the get_results function whether it returns a result"""
		pass

	def test_set_search_criteria(self):
		"""Test the set_search_criteria function whether it allows to give a criteria"""
		pass

	def test_get_results_with_added_token(self):
		"""Test the get_results function whether it accepts a user api token"""
		pass

	def test_get_results_with_multiple_criterias(self):
		"""Test the get_results function whether it gives result with multiple criterias"""
		pass



class weather_app(ABC):
	"""Weather app to do stuff."""


	"""variables"""

	@abstractmethod
	def get_results(self):
		"""gets the results. depending on the search criteria"""
		pass

	@abstractmethod
	def set_search_criteria(self):
		"""Sets the search criterias for large or small pool of results."""
		pass


class OpenWeather_weather_export:
	"""OpenWeather exporting codec."""

	def get_results(self):
		print("get OpenWeather results.")



	def set_search_criteria(self):
		print("Exporting OpenWeather export to show")
		pollingTime = float(input("Polling-Time [s]:"))
		serviceURL = "https://api.openweathermap.org/data/2.5/weather"
		appId = "3836093dde650898eb014e6f27304646"
		while True:
		 responseStr = requests.get(serviceURL + "?q=Uster&units=metric&lang=de&appid=" + appId)
		 jsonResponse = json.loads(responseStr.text)
		 temp = jsonResponse['main']['temp']
		 pressure = jsonResponse['main']['pressure']
		 humidity = jsonResponse['main']['humidity']
		 lon = jsonResponse['coord']['lon']
		 lat = jsonResponse['coord']['lat']
		 cloud = jsonResponse['weather'][0]['description']
		 print(temp, pressure, humidity, lon, lat, cloud)
		 time.sleep(pollingTime)
		 time.sleep(pollingTime)

class Opendata_Swiss_weather_export:
	"""opendata.swiss exporting codec."""

	def get_results(self):
		print("get opendata.swiss results.")

	def set_search_criteria(self):
		print("Exporting opendata.swiss export to show")


class exporter_factory(ABC):
	"""
	Factory that represents a combination of json & xml requests.
	The factory does not maintain any of the instances it createes.
	"""

	@abstractmethod
	def get_data_exporter(self) -> weather_app:
		"""Returns a new weather_call belonging to this factory."""



class good_exporter(exporter_factory):
	"""Factory aimed at providing a good quality export."""

	def get_data_exporter(self) -> weather_app:
		return OpenWeather_weather_export()

class mediocre_exporter(exporter_factory):
	"""Factory aiming at providing a mediocre quality export."""

	def get_data_exporter(self) -> weather_app:
		return Opendata_Swiss_weather_export()



def read_factory() -> exporter_factory:
	"""Construct an exporter factory based on the user's preference."""

	factories = {
		"openweather": good_exporter(),
		"opendataswiss": mediocre_exporter(),
	}
	while True:
		export_format = input("Enter desired output quality (openweather, opendataswiss): ") or "openweather"
		if export_format in factories:
			return factories[export_format]
		print(f"Unknown output quality option: {export_format}.")


def main(fac: exporter_factory) -> None:
	"""Main function."""

	#retreive the exporters
	weather_exporter = fac.get_data_exporter()

	#get the results
	weather_exporter.get_results()

	#sets the search criteria
	weather_exporter.set_search_criteria()






if __name__ == "__main__":

	#create the factory
	factory = read_factory()

	#perform the exporting job
	#main(factory)

	unittest.main()
