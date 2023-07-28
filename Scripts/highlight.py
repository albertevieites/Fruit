import functools

def highlight(series, func, color):
  is_max = series == func(series)
  return [f'background-color: {color}' if v else '' for v in is_max]

hmin = functools.partial(highlight, func=min, color='red') 
hmax = functools.partial(highlight, func=max, color='green')

# display(data.style.apply(hmin).apply(hmax))