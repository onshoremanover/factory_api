

from Lukas_PellegriniA19_DS import *



def main():
	"""Main function."""

	#retreive the exporters
	weather_exporter = fac.get_data_exporter()

	#prepare the export
	weather_exporter.prepare_export()

	#do the export
	weather_exporter.do_export()






if __name__ == "__main__":


	#perform the exporting job
	main()
