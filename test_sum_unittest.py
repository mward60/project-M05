{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "531a7c12",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E\n",
      "======================================================================\n",
      "ERROR: C:\\Users\\kathe\\AppData\\Roaming\\jupyter\\runtime\\kernel-6d0fa6f8-3926-4484-8474-0d924abbb975 (unittest.loader._FailedTest)\n",
      "----------------------------------------------------------------------\n",
      "AttributeError: module '__main__' has no attribute 'C:\\Users\\kathe\\AppData\\Roaming\\jupyter\\runtime\\kernel-6d0fa6f8-3926-4484-8474-0d924abbb975'\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.002s\n",
      "\n",
      "FAILED (errors=1)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "True",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m True\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\kathe\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3465: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "    \n",
    "    def test_sum(self):\n",
    "        self.assertEqual(sum([1, 2, 3]), 6, \"Should be 6\")\n",
    "        \n",
    "    def test_sum_tuple(self):\n",
    "        self.assertEqual(sum((1, 2, 2)), 6, \"Should be 6\")\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64cfd726",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
