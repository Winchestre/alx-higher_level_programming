#include <Python.h>
#include </usr/include/python2.7/pyconfig-64.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size, is_alloc, i;

	size = Py_SIZE(p);
	is_alloc = ((PyListObject *) p)->is_alloc;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", is_alloc);

	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
