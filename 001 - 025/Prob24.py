seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cnt = 0
out = []
for s in seq:
	if s not in out:
		out.append(s)
		for t in seq:
			if t not in out:
				out.append(t)
				for u in seq:
					if u not in out:
						out.append(u)
						for v in seq:
							if v not in out:
								out.append(v)
								for w in seq:
									if w not in out:
										out.append(w)
										for x in seq:
											if x not in out:
												out.append(x)
												for y in seq:
													if y not in out:
														out.append(y)
														for z in seq:
															if z not in out:
																out.append(z)
																for a in seq:
																	if a not in out:
																		out.append(a)
																		for b in seq:
																			if b not in out:
																				out.append(b)
																				if len(out) == len(seq):
																					cnt += 1
																					if cnt%1000 == 0:
																						print(cnt, s,t,u,v,w,x,y,z,a,b)
																					if cnt == 1000000:
																						break
																				del out[-1]
																		del out[-1]
																del out[-1]
														del out[-1]
												del out[-1]
										del out[-1]
								del out[-1]
						del out[-1]
				del out[-1]
		del out[-1]