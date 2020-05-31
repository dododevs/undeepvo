import unittest
import torch
import os
from undeepvo.problems import UnsupervisedDatasetManager
import pykitti
from undeepvo.data import Downloader


sequence_8 = Downloader('08')
# if not os.path.exists(".dataset/"):
#     print("hi")
#     sequence_8.download_sequence()
lengths = (200, 30, 30)
dataset = pykitti.odometry(sequence_8.main_dir, sequence_8.sequence_id, frames=range(0, 260, 1))


class TestUnsupervisedDatasetManager(unittest.TestCase):
    def test_dataset_manager(self):
        dataset_manager = UnsupervisedDatasetManager(dataset, lenghts=lengths)
        self.assertEqual(len(dataset_manager.get_train_dataset()), lengths[0])
        self.assertEqual(len(dataset_manager.get_test_dataset()), lengths[1])
        self.assertEqual(len(dataset_manager.get_validation_dataset()), lengths[2])
        batches = dataset_manager.get_train_batches(20)
        for batch in batches:
            self.assertEqual(batch["left_current_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["right_current_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["left_next_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["right_next_image"].shape, torch.Size([20, 3, 384, 128]))
            break
        batches = dataset_manager.get_validation_batches(20)
        for batch in batches:
            self.assertEqual(batch["left_current_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["right_current_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["left_next_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["right_next_image"].shape, torch.Size([20, 3, 384, 128]))
            break
        batches = dataset_manager.get_test_batches(20)
        for batch in batches:
            self.assertEqual(batch["left_current_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["right_current_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["left_next_image"].shape, torch.Size([20, 3, 384, 128]))
            self.assertEqual(batch["right_next_image"].shape, torch.Size([20, 3, 384, 128]))
            break
