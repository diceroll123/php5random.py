use pyo3::prelude::*;

#[pyclass]
struct Php5Random {
    r: Vec<u32>,
    k: usize,
}

#[pymethods]
impl Php5Random {
    #[new]
    pub fn new(seed: u32) -> Php5Random {
        let mut phpr = Php5Random {
            r: vec![0; 34],
            k: 0,
        };
        phpr.srand(seed);
        phpr
    }

    pub fn srand(&mut self, seed: u32) {
        self.r = vec![0; 34];
        self.r[0] = seed;

        for i in 1..31 {
            self.r[i] = ((16807_u64 * self.r[i - 1] as u64) % 2147483647) as u32;
        }

        for i in 31..34 {
            self.r[i] = self.r[i - 31];
        }

        self.k = 0;

        for _ in 0..310 {
            _ = &self.rand();
        }
    }

    pub fn rand(&mut self) -> u32 {
        let k_as_isize = self.k as isize;
        self.r[self.k] = (self.r[(k_as_isize - 31).rem_euclid(34) as usize] as i64
            + self.r[(k_as_isize - 3).rem_euclid(34) as usize] as i64)
            as u32;
        let r = self.r[self.k] >> 1;
        self.k = (self.k + 1) % 34;
        r
    }

    pub fn rand_range(&mut self, min: u32, max: u32) -> u32 {
        let r = self.rand();
        (min as f64 + ((max as f64 - min as f64 + 1.0) * (r as f64 / 2147483647_f64))) as u32
    }
}

#[pymodule]
fn php5random(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<Php5Random>()?;

    Ok(())
}
