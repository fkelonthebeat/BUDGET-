
class Budget():


  def __init__(self, category):
    self.category = category
    self.balance = 0
    self.transId = 0
    self.transdatabase = {'transIds':[], 'Amount':[], 'transType':[]}

  def _database_update(self, amount, transtype):
      self.transId += 1
      self.transdatabase['transIds'].append(self.transId)
      self.transdatabase['Amount'].append(amount)
      self.transdatabase['transType'].append(transtype)

 
  def _update_balance(self, amount, add= True):
    if add:
      self.balance = ((self.balance) + (amount))
      self._database_update(amount, 'credit')
    else:
      self.balance = ((self.balance) - (amount))
      self._database_update(amount, 'debit')

  def check_balance(self):
    print('Your current balance is {}'.format(self.balance))

  
  def deposit(self, funds):
    try:
      if funds > 0:
        self._update_balance(funds)
        print("Transaction successful")
        self.check_balance()
      else:
        print('Please deposit a valid amount')
    except TypeError:
        print('Please input a number.')
 
 
  def withdrawal(self, amount):
    try:
      if amount > 0 and amount <= self.balance:
        self._update_balance(amount, add= False)
        print("Transaction successful")
        self.check_balance()
      else:
        print('Insufficient money') 
    except TypeError:
      print('Please input a number.')
 
 
  def transfer(self, amount, category2):
    try:    
      if amount <= self.balance:
         self._update_balance(amount, add= False)
         category2._update_balance(amount)
         print("Transaction succesful")
         self.check_balance()
      else:
          print('Insufficient funds!')
    except TypeError:
      print(' Please try again')


  def account_statement(self):
    print('TransactionID'.ljust(20) + 'Amount'.ljust(20) + 'Transaction Type')
    for i in  self.transdatabase['transIds']:  
      print('%s'.ljust(20) %i +'%s'.ljust(20) %self.transdatabase['Amount'][i-1] + '%s' %self.transdatabase['transType'][i-1])
    self.check_balance()
