#!/usr/bin/env python3
import unittest
import tempfile
import os
import sys
import subprocess
import zap


class TestZapFunctionality(unittest.TestCase):

    def test_version_import(self):
        self.assertEqual(zap.__version__, "0.1.0")

    def test_read_requirements_valid_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            temp_path = f.name
            f.write(
                "requests>=2.25.0\nnumpy>=1.20.0\n# This is a comment\n\npandas>=1.3.0"
            )

        try:
            packages = zap.read_requirements(temp_path)
            self.assertEqual(len(packages), 3)
            self.assertIn("requests>=2.25.0", packages)
            self.assertIn("numpy>=1.20.0", packages)
            self.assertIn("pandas>=1.3.0", packages)
        finally:
            try:
                os.unlink(temp_path)
            except (OSError, PermissionError):
                pass

    def test_read_requirements_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            zap.read_requirements("nonexistent_file.txt")

    def test_parse_package_name(self):
        self.assertEqual(zap.parse_package_name("requests>=2.25.0"), "requests")
        self.assertEqual(zap.parse_package_name("numpy==1.20.0"), "numpy")
        self.assertEqual(zap.parse_package_name("pandas"), "pandas")
        self.assertEqual(zap.parse_package_name("scipy<=1.5.0"), "scipy")

    def test_check_installed_packages(self):
        installed = zap.check_installed_packages()
        self.assertIsInstance(installed, set)


class TestZapCLI(unittest.TestCase):

    def test_zap_version_command(self):
        result = subprocess.run(
            [sys.executable, "-m", "zap", "--version"], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("0.1.0", result.stdout)

    def test_zap_help_command(self):
        result = subprocess.run(
            [sys.executable, "-m", "zap", "--help"], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("usage:", result.stdout.lower())

    def test_zap_dry_run_with_sample_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            temp_path = f.name
            f.write("requests>=2.25.0\nnumpy>=1.20.0\n")

        try:
            result = subprocess.run(
                [sys.executable, "-m", "zap", "--dry-run", temp_path],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0)
            self.assertIn("DRY RUN", result.stdout.upper())
            self.assertIn("Requirements Analysis", result.stdout)

        finally:
            try:
                os.unlink(temp_path)
            except (OSError, PermissionError):
                pass

    def test_zap_nonexistent_file(self):
        result = subprocess.run(
            [sys.executable, "-m", "zap", "nonexistent.txt"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
