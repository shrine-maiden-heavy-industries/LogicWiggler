# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages

def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with("")
		else:
			return version.format_choice("+{node}", "+{node}.dirty")
	return {
		"relative_to": __file__,
		"version_scheme": "guess-next-dev",
		"local_scheme": scheme
	}

def doc_ver():
	try:
		from setuptools_scm.git import parse as parse_git
	except ImportError:
		return ""

	git = parse_git(".")
	if not git:
		return ""
	elif git.exact:
		return git.format_with("{tag}")
	else:
		return "latest"

setup(
	name = 'LogicWiggler',
	use_scm_version = vcs_ver(),
	author          = 'Shrine Maiden Heavy Industries',
	author_email    = 'nya@catgirl.link',
	description     = 'A tool and utility to extract logic from PALs and GALs, allowing for archival and reverse engineering',
	license         = 'BSD-3-Clause',
	python_requires = '~=3.8',
	zip_safe        = False,

	setup_requires  = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	install_requires = [
		'Jinja2',
		'construct>=2.10.67',
		'pyusb>=1.2.1',
		'tqdm>=4.62.3',
		'prompt_toolkit>=3.0.20',

		'amaranth @ git+https://github.com/amaranth-lang/amaranth.git@main',
		'amaranth-boards @ git+https://github.com/amaranth-lang/amaranth-boards.git@main',
		'amaranth-stdio @ git+https://github.com/amaranth-lang/amaranth-stdio.git@main',
	],

	packages = find_packages(),
	package_data = {

	},

	extras_require = {
		'toolchain': [
			'amaranth-yosys',
			'yowasp-yosys',
			'yowasp-nextpnr-ice40-8k',
		],

		'firmware': [
			'meson',
		],

		'gui': [
			'PySide2==5.15.2',
		]
	},

	entry_points = {
		'console_scripts': [
			'wigl = logic_wiggler:main',
		],
		'gui_scripts': [
			'wigl-gui = logic_wiggler:main_gui [gui]',
		]
	},

	classifiers = [
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: BSD License',

		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',

		'Topic :: Software Development',
		'Topic :: System :: Hardware',

	],

	project_urls = {
		'Documentation': 'https://github.com/shrine-maiden-heavy-industries/LogicWiggler',
		'Source Code'  : 'hhttps://github.com/shrine-maiden-heavy-industries/LogicWiggler',
		'Bug Tracker'  : 'https://github.com/shrine-maiden-heavy-industries/LogicWiggler/issues',
	}
)
