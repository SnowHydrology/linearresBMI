# linearresBMI

**Description**:  This linear reservoir model includes an implementation of the [Basic Model Interface](https://csdms.colorado.edu/wiki/BMI) (BMI). It's meant for demonstration purposes, but feel free to use it however you like. I'd recommend it mostly for hydrologic modeling, but you do you.

BMI is developed by the [CSDMS](https://csdms.colorado.edu/wiki/Main_Page) group at CU Boulder. Much of the BMI code here is from their [heat](https://github.com/csdms/bmi-example-python) example. 

## Dependencies

This is a simple bit of Python code developed with Python 3.9. The `linearresBMI` module requires:

* The [BMI Python bindings](https://github.com/csdms/bmi-python) from CSDMS
* `numpy`
* `yaml`

The example also requires:

* [Jupyter Notebook](https://jupyter.org/)
* `pandas`
* `Matplotlib`

## Installation

First install the BMI Python bindings using the CSDMS instructions. Next, build the model by going to the main level of the `linearresBMI` directory and running:

`pip install -e .`

## Usage

This model comes with an example Jupyter Notebook so you can see how the BMI functions work to control model execution and the handling of data.

`examples/run-model-from-bmi.ipynb`

To note, the example comes with its own synthetic forcing data, but you can create your own using the R code in `tools`.

## Known issues

This is but a simple model that makes several assumptions. They are:

* All incoming precipitation (or land surface water flux) is liquid
* Discharge is the only way to leave the reservoir (i.e., there is no evapotranspiration)
* The model is configured for a daily timestep and there is no explicit handling of POSIX-formatted datetimes

## Reporting issues, getting help

If you see any bugs, errors, etc., please use this repo's Issue Tracker. You can also make any requests for help there.

## Open source licensing info
[LICENSE](LICENSE)

----

## Credits and references

1. [BMI](https://csdms.colorado.edu/wiki/BMI) from CSDMS
2. The BMI Python [heat](https://github.com/csdms/bmi-example-python) example
3. Wikipedia's entry on [runoff models](https://en.wikipedia.org/wiki/Runoff_model_(reservoir)) (yes, that Wikipedia)
   - The linear reservoir equation cites this document: *J.W. de Zeeuw, 1973. Hydrograph analysis for areas with mainly groundwater runoff. In: Drainage Principle and Applications, Vol. II, Chapter 16, Theories of field drainage and watershed runoff. p 321-358. Publication 16, International Institute for Land Reclamation and Improvement (ILRI), Wageningen, The Netherlands.* (good luck finding it!)
4. The Next Generation Water Prediction Capability project at the NOAA-NWS Office of Water Prediction
   - GitHub repo for the [NextGen Framework](https://github.com/NOAA-OWP/ngen)
   - BMI implementation of the [LSTM](https://github.com/NOAA-OWP/lstm/) machine learning model
