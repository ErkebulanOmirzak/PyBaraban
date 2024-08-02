// ffi.rs

use libc;

extern "C" {
    fn generate_storyboard(osufile: *const libc::c_char, osbfile: *const libc::c_char, resourcefolder: *const libc::c_char) -> libc::c_int;
}

pub fn generate_storyboard_rust(osufile: &str, osbfile: &str, resourcefolder: &str) -> Result<(), String> {
    let osufile_c = std::ffi::CString::new(osufile).unwrap();
    let osbfile_c = std::ffi::CString::new(osbfile).unwrap();
    let resourcefolder_c = std::ffi::CString::new(resourcefolder).unwrap();

    unsafe {
        let result = generate_storyboard(
            osufile_c.as_ptr(),
            osbfile_c.as_ptr(),
            resourcefolder_c.as_ptr(),
        );

        if result == 0 {
            Ok(())
        } else {
            Err("Failed to generate storyboard".to_string())
        }
    }
}
