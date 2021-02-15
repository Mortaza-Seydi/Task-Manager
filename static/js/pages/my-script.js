// Class definition

var KTFormWidgetsValidation = function () {
    // Private functions
    var validator;


    var _initWidgets = function () {
        // Initialize Plugins

        $('#kt_datepicker_3, #kt_datepicker_3_validate').datepicker({
            rtl: false,
            format: 'yyyy-mm-dd',
            todayBtn: "linked",
            clearBtn: true,
            todayHighlight: true,
            templates: {
                leftArrow: '<i class="la la-angle-left"></i>',
                rightArrow: '<i class="la la-angle-right"></i>'
            }
        }).on('changeDate', function (e) {
            // Revalidate field
            validator.revalidateField('date');
        });

        // Select2
        $('#kt_select2_3').select2({
            placeholder: "Select a user",
        });

        $('#kt_select2_3').on('change', function () {
            // Revalidate field
            validator.revalidateField('users');
        });

        $('#iname').on('change', function () {
            // Revalidate field
            validator.revalidateField('name');
        });

        $('#idesc').on('change', function () {
            // Revalidate field
            validator.revalidateField('desc');
        });

        $('#idetails').on('change', function () {
            // Revalidate field
            validator.revalidateField('details');
        });

    }

    var _initValidation = function () {
        // Validation Rules
        validator = FormValidation.formValidation(
            document.getElementById('add_board_from'),
            {
                fields: {
                    name: {
                        validators: {
                            notEmpty: {
                                message: 'Name is required'
                            },
                            stringLength: {
                                min: 1,
                                max: 50,
                                message: 'Please enter a menu within text length range 1 and 50'
                            }
                        }
                    },
                    desc: {
                        validators: {
                            notEmpty: {
                                message: 'Description is required'
                            },
                            stringLength: {
                                min: 1,
                                max: 200,
                                message: 'Please enter a menu within text length range 1 and 200'
                            }
                        }
                    },
                    details: {
                        validators: {
                            notEmpty: {
                                message: 'Details is required'
                            },
                            stringLength: {
                                min: 1,
                                max: 1000,
                                message: 'Please enter a menu within text length range 1 and 1000'
                            }
                        }
                    },
                    date: {
                        validators: {
                            notEmpty: {
                                message: 'Date is required'
                            }
                        }
                    },
                    users: {
                        validators: {
                            notEmpty: {
                                message: 'Users is required'
                            }
                        }
                    },
                },

                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),

                    // Validate fields when clicking the Submit button
                    submitButton: new FormValidation.plugins.SubmitButton(),

                    // Submit the form when all fields are valid
                    // defaultSubmit: new FormValidation.plugins.DefaultSubmit(),

                    bootstrap: new FormValidation.plugins.Bootstrap()

                }
            }
        );

        $('#psubmit').on('click', function (e, options) {
            options = options || {};

            if (!options.flag) {
                e.preventDefault();

                validator.validate().then(function (status) {
                    if (status == 'Valid') {
                        swal.fire({
                            text: "All is cool! Now we submitted data to the Server",
                            icon: "success",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn font-weight-bold btn-light-primary"
                            }
                        }).then(function () {
                            $('#psubmit').trigger('click', {flag: true});
                        });
                    } else {
                        swal.fire({
                            text: "Sorry, looks like there are some errors detected, please try again.",
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn font-weight-bold btn-light-primary"
                            }
                        }).then(function () {
                            KTUtil.scrollTop();
                        });
                    }
                });
            } else {
                $("#add_board_from").submit();
            }
        });
    }

    return {
        // public functions
        init: function () {
            _initWidgets();
            _initValidation();
        }
    };
}();

jQuery(document).ready(function () {
    KTFormWidgetsValidation.init();
});
