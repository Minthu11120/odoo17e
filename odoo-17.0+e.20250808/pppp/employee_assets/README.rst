Employee Asset Request Management
Overview

The Employee Asset Request Management module provides a complete workflow for managing employee asset requests inside Odoo.
It allows employees to request company assets, managers to approve them, and administrators to assign physical assets while maintaining accurate availability tracking.

This module is designed to work directly with account.asset, without introducing a separate asset type model.

Key Features
Employee Asset Requests

Employees can create asset requests for available company assets

Request is automatically linked to the logged-in employee

Quantity validation to prevent invalid requests

Request lifecycle tracking with clear states

Approval Workflow

Employee → Manager → Assignment

Manager approval visible only to the selected manager

Status tracking via chatter (mail.thread)

Asset Assignment

Assign available assets using a wizard

Prevent assignment of already assigned assets

Automatically update asset state (available → assigned)

Store assigned date and assigned assets

Supports assets grouped by model_id inside account.asset

Security & Access Control

Employees see only their own requests

Managers can see all requests

Approve / Reject buttons appear only for authorized users

Proper record rules and groups included

Mail & Activities

Email notification when request is submitted

Automatic mail activity created for manager approval

Activities are linked only to this model (not mixed with others)

Reporting

List view with default descending order

Pivot and list views for asset assignment reporting

Excel export supported via Odoo standard features

Tree view grouped by employee

Workflow States

Draft – Employee creates request

Submitted – Request sent to manager

Manager Approved – Approved by manager

Assigned – Assets assigned successfully

Rejected – Request rejected

Technical Details
Models

employee.assets.request

Uses existing account.asset model

No additional asset type model required

Key Fields

employee_id – Auto-set from logged-in user

manager_id – Derived from employee hierarchy

asset_type – Selected from available account.asset

assigned_asset_ids – Many2many assigned assets

assigned_date – Assignment timestamp

state – Workflow status

Installation

Copy the module into your custom addons directory

Restart Odoo server

Activate Developer Mode

Install Employee Asset Request Management

Configuration

Ensure employees are linked to users (hr.employee.user_id)

Managers must have user accounts

Assets must exist in account.asset

Asset availability is controlled by asset state

Compatibility

Odoo 17.0

Community & Enterprise

Use Cases

Internal IT asset requests (Laptop, Phone, Monitor)

Office equipment tracking

Employee onboarding asset management

Asset accountability and reporting

License

LGPL-3