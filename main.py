from hh_p import hh_get_jobs
from so import so_get_jobs
from save import save_to_scv
 
hh_jobs = hh_get_jobs()
so_jobs = so_get_jobs()
print(so_jobs)

jobs = hh_jobs + so_jobs
save_to_scv(jobs)






