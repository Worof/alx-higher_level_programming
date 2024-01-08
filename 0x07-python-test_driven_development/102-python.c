#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
#include <stdio.h>
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UNICODE *unicode = PyUnicode_AsUnicode(p);
    int is_ascii = PyUnicode_IS_ASCII(p);

    printf("[.] string object info\n");
    if (is_ascii)
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    printf("  length: %zd\n", length);
    printf("  value: %ls\n", unicode);
}
