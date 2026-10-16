import unittest
from unittest.mock import patch
from yummy_app import YummyApp
import gps_service


class TestEasyLevel(unittest.TestCase):
    def setUp(self):
        self.app = YummyApp()

    def test_calculate_total_for_single_item(self):
        self.assertEqual(self.app.calculate_order_total({"pho": 2}), 100000)

    def test_calculate_total_for_multiple_items(self):
        self.assertEqual(self.app.calculate_order_total({"pho": 1, "bun": 1}), 95000)

    def test_calculate_total_for_empty_cart(self):
        self.assertEqual(self.app.calculate_order_total({}), 0.0)

    def test_calculate_total_with_zero_quantity(self):
        self.assertEqual(self.app.calculate_order_total({"pho": 0}), 0.0)

    def test_calculate_total_ignores_unknown_and_negative_quantity(self):
        self.assertEqual(
            self.app.calculate_order_total({"unknown": 4, "com": -2}), 0.0
        )

    def testphobosaurieng(self):
        """Test mon bo sung phobosaurieng co gia 999000 theo de bai."""
        self.assertEqual(
            self.app.calculate_order_total({"phobosaurieng": 1}), 999000
        )


class TestMediumLevel(unittest.TestCase):
    def test_promo_online_valid_giam10(self):
        app = YummyApp(network_status="online", os_version=14)
        self.assertEqual(app.apply_promo_code(100000, "GIAM10"), 90000)

    def test_promo_offline_raises_connection_error(self):
        app = YummyApp(network_status="offline")
        with self.assertRaises(ConnectionError):
            app.apply_promo_code(100000, "GIAM10")

    def test_new_os_promo_on_os15(self):
        app = YummyApp(os_version=15)
        self.assertEqual(app.apply_promo_code(100000, "NEW_OS_ONLY"), 80000)

    def test_new_os_promo_on_os14_raises_value_error(self):
        app = YummyApp(os_version=14)
        with self.assertRaises(ValueError):
            app.apply_promo_code(100000, "NEW_OS_ONLY")

    def test_unknown_promo_raises_value_error(self):
        app = YummyApp()
        with self.assertRaises(ValueError):
            app.apply_promo_code(100000, "NOT_REAL")


class TestHardLevel(unittest.TestCase):
    @patch("yummy_app.gps_service.get_current_location", return_value=(10.0, 105.0))
    def test_gps_inside_known_area(self, mock_gps):
        app = YummyApp()
        self.assertEqual(
            app.get_nearby_restaurants(),
            ["Nha hang Pho Ly Quoc Su", "Bun cha Huong Lien"],
        )
        mock_gps.assert_called_once_with()

    @patch("yummy_app.gps_service.get_current_location", return_value=(20.0, 110.0))
    def test_gps_outside_known_area_returns_empty_list(self, mock_gps):
        app = YummyApp()
        self.assertEqual(app.get_nearby_restaurants(), [])
        mock_gps.assert_called_once_with()

    @patch(
        "yummy_app.gps_service.get_current_location",
        side_effect=gps_service.GPSSignalLostError("GPS lost"),
    )
    def test_gps_signal_lost_returns_message(self, mock_gps):
        app = YummyApp()
        self.assertEqual(app.get_nearby_restaurants(), "Khong the xac dinh vi tri.")
        mock_gps.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
