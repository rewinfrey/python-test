class A:
  def b(self):
    return c

  def c(self):
      return d

  @a
  @b
  @c
  def d(self):
      return e
