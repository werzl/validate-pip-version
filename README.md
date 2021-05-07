<div align="center">
  
# validate-pip-version
CLI tool to validate the version of a local PIP package against its currently published version. Intended to be used as part of a CI build.
  
[![CI](https://github.com/werzl/validate-pip-version/actions/workflows/CI.yml/badge.svg)](https://github.com/werzl/validate-pip-version/actions/workflows/CI.yml)
[![CD](https://github.com/werzl/validate-pip-version/actions/workflows/CD.yml/badge.svg)](https://github.com/werzl/validate-pip-version/actions/workflows/CD.yml)
  
</div>

# Installation
First Install:
  
```
pip install validate-pip-version
```
  
Upgrading
```
pip install validate-pip-version --upgrade
```
  
# GitHub Actions Example
https://github.com/werzl/validate-pip-version/blob/master/.github/workflows/CI.yml
  
# Usage
```
validate_pip_version [OPTIONS] COMMAND [ARGS]
```
  
## check-init-file
Retrieves the local package version from an __init__.py, by matching the string '`__version__`'.
```
validate_pip_version check-init-file -n <package_name> --init_file_path <path_to__init__.py>
```
  
### Options
<table>
	<thead>
		<tr>
			<th>Option</th>
			<th>Required</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>-n, --package_name</td>
			<td>Required</td>
			<td>Name of the package on PyPi</td>
		</tr>
		<tr>
			<td>--init_file_path</td>
			<td>Required</td>
			<td>Relative file path for the __init__.py file<br/>(uses current working dir)</td>
		</tr>
		<tr>
			<td>--help</td>
			<td>Optional</td>
			<td>Show help message and exit</td>
		</tr>
	</tbody>
</table>
  
<br/><hr/><br/>
  
## check-setup-file
Retrieves the local package version from an setup.py file, by matching the string '`version=`' and stripping away spaces/newlines.
```
validate_pip_version check-setup-file -n <package_name> --init_file_path <path_to_setup.py>
```
  
### Options
<table>
	<thead>
		<tr>
			<th>Option</th>
			<th>Required</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>-n, --package_name</td>
			<td>Required</td>
			<td>Name of the package on PyPi</td>
		</tr>
		<tr>
			<td>--setup_file_path</td>
			<td>Required</td>
			<td>Relative file path for the setup.py file<br/>(uses current working dir)</td>
		</tr>
		<tr>
			<td>--help</td>
			<td>Optional</td>
			<td>Show help message and exit</td>
		</tr>
	</tbody>
</table>
