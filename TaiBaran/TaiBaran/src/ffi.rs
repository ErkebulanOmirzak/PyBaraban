// src/ffi.rs

use std::ffi::CString;

extern "C" {
    fn generate_storyboard(osufile: *const libc::c_char, osbfile: *const libc::c_char, resourcefolder: *const libc::c_char) -> libc::c_int;
}

pub fn generate_storyboard(osufile: &str, osbfile: &str, resourcefolder: &str) -> Result<(), String> {
    let osufile_c = CString::new(osufile).map_err(|e| e.to_string())?;
    let osbfile_c = CString::new(osbfile).map_err(|e| e.to_string())?;
    let resourcefolder_c = CString::new(resourcefolder).map_err(|e| e.to_string())?;

    let result = unsafe {
        generate_storyboard(
            osufile_c.as_ptr(),
            osbfile_c.as_ptr(),
            resourcefolder_c.as_ptr()
        )
    };

    if result == 0 {
        Ok(())
    } else {
        Err("Failed to generate storyboard".into())
    }
}