import unittest
from zookeeper import Ztree


class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    def test_borrar_nodo_inexistente(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.delete('/node1/node2/node3', 1)

    def test_borrar_nodo_version_no_concuerda(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1', 'algo', True, True, 10, '/')
            tree.delete('/node1', 2)

    def test_set_data(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

        tree.setData('/node1', 'hola')
        self.assertEqual(tree.getData('/node1'), 'hola')

    def test_set_data_nodo_inexistente(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.setData('/node1', 'hola')

    def test_set_data_nueva_version(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.get_tree().get_node('/node1').data.version, 0)

        tree.setData('/node1', 'hola')
        self.assertEqual(tree.get_tree().get_node('/node1').data.version, 1)


if __name__ == '__main__':
    unittest.main()
