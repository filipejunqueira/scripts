from nexusformat.nexus import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def get_nexus_data(file, entry_string="entry1", detector="ew4000"):
    try:
        start_time = file[entry_string]["start_time"].nxvalue
        end_time = file[entry_string]['end_time'].nxvalue
        region_name_list = file[entry_string]["instrument"][detector]["region_list"].nxvalue
        region_name_list = region_name_list.split(",")
    except:
        pass

    metadata_region_list = []
    data_region_list = []

    for region in region_name_list:
        attributes = file[entry_string]["instrument"][region]
        spectrum_data = file[entry_string]["instrument"][region].spectrum_data.nxvalue  # Y data
        energies = file[entry_string]["instrument"][region].energies.nxvalue  # X data
        acquisition_mode = file[entry_string]["instrument"][region].acquisition_mode.nxvalue
        angles = file[entry_string]["instrument"][region].angles.nxvalue
        energy_mode = file[entry_string]["instrument"][region].energy_mode.nxvalue
        energy_step = file[entry_string]["instrument"][region].energy_step.nxvalue
        excitation_energy = file[entry_string]["instrument"][region].excitation_energy.nxvalue
        external_io_data = file[entry_string]["instrument"][region].external_io_data.nxvalue
        fixed_energy = file[entry_string]["instrument"][region].fixed_energy.nxvalue
        high_energy = file[entry_string]["instrument"][region].high_energy.nxvalue
        image_data = file[entry_string]["instrument"][region].image_data.nxvalue
        lens_mode = file[entry_string]["instrument"][region].lens_mode.nxvalue
        local_name = file[entry_string]["instrument"][region].local_name.nxvalue
        low_energy = file[entry_string]["instrument"][region].low_energy.nxvalue
        number_of_iterations = file[entry_string]["instrument"][region].number_of_iterations.nxvalue
        number_of_slices = file[entry_string]["instrument"][region].number_of_slices.nxvalue
        pass_energy = file[entry_string]["instrument"][region].pass_energy.nxvalue
        step_time = file[entry_string]["instrument"][region].step_time.nxvalue
        total_steps = file[entry_string]["instrument"][region].total_steps.nxvalue
        total_time = file[entry_string]["instrument"][region].total_time.nxvalue
        external_io_data = file[entry_string]["scaler2"]["sm5amp8"].nxvalue
        #print(f"Metadata found are for file {file_name}: acquisition mode: {acquisition_mode}, angle: {angles}, energy mode: {energy_mode}, energy step: {energy_step}, excitation energy: {excitation_energy}, fixed energy: {fixed_energy}, high energy: {high_energy}, lens mode: {lens_mode}, local name: {local_name}, low energy: {low_energy}, number of iterations: {number_of_iterations}, number of slices: {number_of_slices}, pass energy: {pass_energy}, step time: {step_time}, total steps: {total_steps}, total time: {total_time}")

        metadata_region_list.append({"acquisition_mode": acquisition_mode, "angles": angles, "energy_mode": energy_mode,
                    "energy_step": energy_step, "excitation_energy": excitation_energy, "fixed_energy": fixed_energy,
                    "high_energy": high_energy, "lens_mode": lens_mode, "local_name": local_name,
                    "low_energy": low_energy, "number_of_iterations": number_of_iterations,
                    "number_of_slices": number_of_slices, "pass_energy": pass_energy, "step_time": step_time,
                    "total_steps": total_steps, "total_time": total_time, "start_time": start_time, "end_time": end_time, "energies": energies,
                    "spectrum_data": spectrum_data, "region_name": region, "attributes": attributes})
        data_region_list.append({"energies": energies, "spectrum_data": spectrum_data, "image_data": image_data, "i0": external_io_data})

    return data_region_list, metadata_region_list


if __name__ == "__main__":

    print("DONT RUN ME, I AM A MODULE")



