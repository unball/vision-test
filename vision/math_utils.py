def normToAbs(normPoint, shape):
  """Método que recebe um ponto \\(p=(x,y)\\) em um sistema de coordenadas normalizado \\(0\\leq x,y \\leq 1\\) e passa para um sistema de coordenadas absoluto em pixels de acordo com `shape`: \\(s=(h,w)\\), pela fórmula: \\((w\\cdot x, h\\cdot y)\\)"""
  return (round(normPoint[0]*shape[1]), round(normPoint[1]*shape[0]))
