#!/usr/bin/env python

"""Tests for `synology_plex_manager` package."""


import unittest
from click.testing import CliRunner

from synology_plex_manager import synology_plex_manager
from synology_plex_manager import cli


class TestSynology_plex_manager(unittest.TestCase):
    """Tests for `synology_plex_manager` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'synology_plex_manager.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
